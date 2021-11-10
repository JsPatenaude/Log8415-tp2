import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

DATASET_INDEX = 0
N_DATASETS = 9
N_PASS = 3

def read_results(filename):
    # Return results in a readable format (Dataset, pass number and user time in seconds)
    with open(filename) as file:
        lines = file.readlines()
        results_lines = []
        for i, line in enumerate(lines):
            if line.startswith(' Dataset'):
                result_line = line.replace('\n', ', ') + lines[i + 1].replace('\n', '').replace('\t', ' ').replace('0m', '').replace('\n', ' ')
                results_lines.append(result_line[1:-1])
        results = []
        for result in results_lines:
            dataset = int(result.split('Dataset ')[1].split(', ')[0])
            pass_number = int(result.split('pass ')[1].split(', ')[0])
            user_time = float(result.split('user ')[1].split(', ')[0])
            results.append([dataset, pass_number, user_time])
        return results


def plot_results_specific_dataset(x_hadoop, y_hadoop, x_spark, y_spark, dataset_index):
    plt.plot(x_hadoop, y_hadoop, label = "Hadoop time results")
    plt.plot(x_spark, y_spark, label = "Spark time results")
    plt.title(f'User times for each pass on Hadoop and Spark for the dataset {dataset_index}')
    plt.xlabel('Pass Number')
    plt.ylabel('User Time (s)')
    plt.scatter(x_hadoop, y_hadoop)
    plt.scatter(x_spark, y_spark)
    plt.xticks(x_hadoop)
    plt.legend(loc="center left")
    # plt.show()
    plt.savefig(f'graphs/times_for_dataset_{dataset_index}.png')
    plt.clf()


def plot_results_averages(y_hadoop, y_spark):
    x_hadoop = np.array([i for i in range(1, N_DATASETS + 1)])
    x_spark = np.array([i for i in range(1, N_DATASETS + 1)])
    plt.plot(x_hadoop, y_hadoop, label = "Hadoop average times")
    plt.plot(x_spark, y_spark, label = "Spark average times")
    plt.title(f'Average user times for each dataset on Hadoop and Spark')
    plt.xlabel('Dataset Number')
    plt.ylabel('Average User Time (s)')
    plt.scatter(x_hadoop, y_hadoop)
    plt.scatter(x_spark, y_spark)
    plt.xticks(x_hadoop)
    plt.legend(loc="center left")
    # plt.show()
    plt.savefig('graphs/average_times.png')
    plt.clf()


def main():
    results_hadoop = read_results("results_hadoop_wordcount.txt")
    results_spark = read_results("results_spark_wordcount.txt")
    hadoop_average_times = []
    spark_average_times = []
    for i in range(1, N_DATASETS + 1):
        results_hadoop_specific_dataset = []
        results_spark_specific_dataset = []
        for result_hadoop in results_hadoop:
            if result_hadoop[DATASET_INDEX] == i:
                results_hadoop_specific_dataset.append(result_hadoop)
        for result_spark in results_spark:
            if result_spark[DATASET_INDEX] == i:
                results_spark_specific_dataset.append(result_spark)
        # Results as numpy arrays
        x_hadoop = np.array([i for i in range(N_PASS)])
        y_hadoop = np.array([i[2:] for i in results_hadoop_specific_dataset]).flatten()
        x_spark = np.array([i for i in range(N_PASS)])
        y_spark = np.array([i[2:] for i in results_spark_specific_dataset]).flatten()
        # Plot graph for specific dataset
        plot_results_specific_dataset(x_hadoop, y_hadoop, x_spark, y_spark, i)
        # Average times for Hadoop and Spark for each dataset
        hadoop_average_times.append(round(np.mean(y_hadoop), 3))
        spark_average_times.append(round(np.mean(y_spark), 3))
    plot_results_averages(hadoop_average_times, spark_average_times)
    # Print the average times for Hadoop and Spark
    hadoop_average = round(np.mean(hadoop_average_times), 3)
    spark_average = round(np.mean(spark_average_times), 3)
    print("Hadoop average: ", hadoop_average)
    print("Spark average: ", spark_average)


if __name__ == "__main__":
    main()
