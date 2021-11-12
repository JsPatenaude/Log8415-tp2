from collections import Counter
import itertools
from pyspark.sql import *
from pyspark.sql.functions import *


# create the Spark Session
spark = SparkSession.builder.getOrCreate()

# create the Spark Context
sc = spark.sparkContext

data = sc.textFile("./soc-LiveJournal1Adj.txt")
N = 10 # number of friends to recommends

def textParser(line):
    split = line.split()
    id = split[0]

    relations = []
    if len(split) == 2:
        relations = split[1].split(',')
    
    # indirect Pair (relation[n] -> relationW[n+1])
    pairs = [(pair, (False, 1)) for pair in itertools.permutations(relations, 2)]
    # direct pair (user -> relation)
    relations = [((id,r), (True, 1)) for r in relations]
    
    return pairs + relations

def reduceConnections(userA,userB):
    return (userA[0] or userB[0], userA[1]+userB[1] )


def map(user):
    tmp = [(pair[0], pair[1]) for pair in user[1]]
    tmp.sort(key=lambda x: x[1], reverse=True) # sort by number of connections
    return (user[0],tmp[:N])

# user[0][0] = userId
# user[0][1] = user2Id
# user[1][0] = isAlreadyFriend
# user[1][1] = nFriendCommon

data = data.flatMap(textParser) # Parse Text
data = data.reduceByKey(reduceConnections) # Reduce similar connections to one
data = data.filter(lambda data : data[1][0] == False) # Remove if already friends
data = data.map(lambda user: (user[0][0],(user[0][1],user[1][1]))) # Change to key = user, data=(friendId, numberOfMutualFriends)
data = data.groupByKey() # Reduce User
data = data.map(map) # Sort friends

users = ["924", "8941", "8942", "9019", "9020", "9021", "9022", "9990", "9992", "9993"]
print("User: <id> Friends : [<id>(<numberOfConnection>)]")
for user in users:
    print("User: " + user + " Friends : ", end = '')
    for friend, connection in data.lookup(user)[0]:
        print(friend+"("+ str(connection) +")", end = ' ')
    print('')
