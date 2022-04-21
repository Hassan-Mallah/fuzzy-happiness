import pandas as pd
from pandas import DataFrame


def pd_version():
    print('version:', pd.__version__, '\n')


# get data from csv file
def from_csv(file_name) -> DataFrame:
    return pd.read_csv(file_name)


def print_dataframe(df: DataFrame):
    print(df)


# n amount of top rows
def get_top_rows(df: DataFrame, n):
    print(df.head(n))


# n amount of top rows
def get_last_rows(df: DataFrame, n):
    print(df.tail(n))


def save_to_excel(df, file_name, sheet_name):
    df.to_excel(file_name, sheet_name=sheet_name, index=False)


# get DataFrame from excel file
def from_excel(file_name, sheet_name) -> DataFrame:
    return pd.read_excel(file_name, sheet_name)


titanic = from_excel("titanic.xlsx", sheet_name="passengers")
print(titanic)
