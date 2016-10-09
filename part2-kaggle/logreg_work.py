import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import pylab


DATASET_TRAINING = "./titanic-dataset/train.csv"
DATASET_TEST = "./titanic-dataset/test.csv"

OUTPUT_RESULT = "./output/logreg.csv"

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

    df_train = pd.read_csv(DATASET_TRAINING, header=0)
    df_test = pd.read_csv(DATASET_TEST, header=0)
    df_survived = df_train['Survived']
    df_test_id = df_test['PassengerId']

    for df in [df_train, df_test]:
        # Change from label to numeric value
        df['S_Gender'] = df["Sex"].map(lambda x: 0 if x == "male" else 1)
        # Fill missing values in age
        median_age = df_train["Age"].median()
        df['S_AgeFill'] = df["Age"]
        df.loc[ df['Age'].isnull(), 'S_AgeFill'] =  median_age
        # Add new feature that tells when age was missing
        df['S_AgeNull'] = pd.isnull(df['Age']).astype(int)
        #print(df.describe())
        # Problem with Fare, putting mean if missing (only 1)
        mean_fare = df_train["Fare"].mean()
        df['S_Fare'] = df["Fare"]
        df.loc[df['Fare'].isnull(), 'S_Fare'] = mean_fare
        # print(df.describe())

    df_train = df_train[['Pclass', 'S_Fare', 'S_Gender', 'S_AgeFill', 'S_AgeNull']]
    df_test = df_test[['Pclass', 'S_Fare', 'S_Gender', 'S_AgeFill', 'S_AgeNull']]

    survival = df_survived.values
    train = df_train.values
    test = df_test.values

    lgr = LogisticRegression()
    lgr = lgr.fit(train, survival)
    result = lgr.predict(test)
    id = df_test_id.values
    result = np.stack((id, result), axis=-1)
    print(result)

    return result


def main():
    csv_dataset_train = load_csv_dataset(DATASET_TRAINING)
    csv_dataset_test = load_csv_dataset(DATASET_TEST)
    result = predict(csv_dataset_train, csv_dataset_test)
    save_result(result)


if __name__ == '__main__':
    main()


