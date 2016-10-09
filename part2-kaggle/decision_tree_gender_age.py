import csv
import pandas as pd
from sklearn import tree
import numpy as np


DATASET_TRAINING = "./titanic-dataset/train.csv"
DATASET_TEST = "./titanic-dataset/test.csv"

OUTPUT_RESULT = "./output/gender_age_tree.csv"

TEST_INDEX_PASSENGER_ID = 0
TEST_INDEX_GENRE = 3
TEST_INDEX_AGE = 4
TRAIN_INDEX_PASSENGER_ID = 0
TRAIN_INDEX_SURVIVED = 1
TRAIN_INDEX_GENRE = 4
TRAIN_INDEX_AGE = 5

def load_csv_dataset(filename):
    with open(filename, "rb") as input_file:
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


def predict(csv_train, csv_test):
    # Training
    data_train = np.array(csv_train)
    data_test = np.array(csv_test)
    # Change from label to numeric value
    data_train[data_train == 'male'] = 0
    data_train[data_train == 'female'] = 1
    data_test[data_test == 'male'] = 0
    data_test[data_test == 'female'] = 1
    # Some age are missing, putting an arbitrary value
    data_train[data_train[0::,TRAIN_INDEX_AGE] == '', TRAIN_INDEX_AGE] = 30
    data_test[data_test[0::,TEST_INDEX_AGE] == '', TEST_INDEX_AGE] = 30

    #print(data_train[0::,[TRAIN_INDEX_PASSENGER_ID, TRAIN_INDEX_GENRE, TRAIN_INDEX_AGE]])
    survival = data_train[0::,TRAIN_INDEX_SURVIVED]
    train = data_train[0::,[TRAIN_INDEX_GENRE, TRAIN_INDEX_AGE]].astype(np.float)
    test =  data_test[0::,[TEST_INDEX_GENRE, TEST_INDEX_AGE]].astype(np.float)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train, survival)
    result = clf.predict(test)
    result = np.stack((data_test[0::, TEST_INDEX_PASSENGER_ID], result), axis=-1)
    #print(result)

    return result


def main():
    csv_dataset_train = load_csv_dataset(DATASET_TRAINING)
    csv_dataset_test = load_csv_dataset(DATASET_TEST)
    result = predict(csv_dataset_train, csv_dataset_test)
    save_result(result)


if __name__ == '__main__':
    main()


