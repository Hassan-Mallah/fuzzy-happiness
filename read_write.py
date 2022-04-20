import pandas as pd
from pandas import DataFrame


def pd_version():
    print('version:', pd.__version__, '\n')


def print_titanic(df: DataFrame):
    print(df)


# n amount of top rows
def get_top_rows(df: DataFrame, n):
    print(df.head(n))


# n amount of top rows
def get_last_rows(df: DataFrame, n):
    print(df.tail(n))


def save_to_excel(df, file_name, sheet_name):
    df.to_excel(file_name, sheet_name=sheet_name, index=False)


titanic = pd.read_csv("data/titanic.csv")

get_last_rows(titanic, 5)
