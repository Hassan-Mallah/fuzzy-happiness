import pandas as pd


def pd_version():
    print('version:', pd.__version__, '\n')


def print_titanic(titanic):
    print(titanic)


titanic = pd.read_csv("data/titanic.csv")

# [891 rows x 12 columns]
print_titanic(titanic)
