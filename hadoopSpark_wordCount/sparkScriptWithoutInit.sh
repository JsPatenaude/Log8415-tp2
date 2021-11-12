touch timeSpend.txt
for i in {0..2}
do
  hdfs dfs -rm -r datasetProcessed1$i$i
  hdfs dfs -rm -r datasetProcessed2$i$i
  hdfs dfs -rm -r datasetProcessed3$i$i
  hdfs dfs -rm -r datasetProcessed4$i$i
  hdfs dfs -rm -r datasetProcessed5$i$i
  hdfs dfs -rm -r datasetProcessed6$i$i
  hdfs dfs -rm -r datasetProcessed7$i$i
  hdfs dfs -rm -r datasetProcessed8$i$i
  hdfs dfs -rm -r datasetProcessed9$i$i
  echo " Dataset 1, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/4vxdw3pa 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 2, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/kh9excea datasetProcessed2$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 3, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/dybs9bnk datasetProcessed3$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 4, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/datumz6m datasetProcessed4$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 5, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/j4j4xdw6 datasetProcessed5$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 6, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/ym8s5fm4 datasetProcessed6$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 7, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/2h6a75nk datasetProcessed7$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 8, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/vwvram8  datasetProcessed8$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
  echo " Dataset 9, pass $i" >> timeSpend.txt
  ./bin/spark-submit \
  --class org.apache.spark.examples.JavaWordCount \
  --master local[4] \
  --executor-memory 15G \
  examples/jars/spark-examples_2.12-3.2.0.jar \
  hdfs://localhost:9000/user/azureuser/dataset/tmp/weh83uyn datasetProcessed9$i$i 2> >((grep " ms \| s ") >> timeSpend.txt)
done