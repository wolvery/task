import pandas as pd


def get_data_frame():
    return pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/00334/wiki4HE.csv", sep=";")
