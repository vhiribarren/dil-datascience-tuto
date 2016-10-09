import csv
import numpy as np


DATASET_TRAINING = "./titanic-dataset/train.csv"
DATASET_TEST = "./titanic-dataset/test.csv"

OUTPUT_RESULT = "./output/gender_model.csv"

TEST_INDEX_PASSENGER_ID = 0
TEST_INDEX_GENRE = 3


def load_dataset_test():
    with open(DATASET_TEST, "rb") as input_file:
        csv_data = csv.reader(input_file)
        csv_data.next()
        dataset = []
        for row in csv_data:
            dataset.append(row)
        return dataset


def save_result(data):
    with open(OUTPUT_RESULT, "wb") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(["PassengerId", "Survived"])
        for row in data:
            csv_writer.writerow(row)


def predict(dataset):
    result = []
    for row in dataset:
        if row[TEST_INDEX_GENRE] == "female":
            result.append([row[TEST_INDEX_PASSENGER_ID], 1])
        else:
            result.append([row[TEST_INDEX_PASSENGER_ID], 0])
    return result


def main():
    csv_dataset = load_dataset_test()
    result = predict(csv_dataset)
    save_result(result)


if __name__ == '__main__':
    main()


