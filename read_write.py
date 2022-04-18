import pandas as pd


def pd_version():
    print('version:', pd.__version__, '\n')


def print_titanic(df):
    print(df)


def get_top_rows(df, n):
    print(df.head(n))


titanic = pd.read_csv("data/titanic.csv")

get_top_rows(titanic, 1)
