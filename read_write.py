import pandas as pd


def pd_version():
    print('version:', pd.__version__, '\n')


def print_titanic(df):
    print(df)


# n amount of top rows
def get_top_rows(df, n):
    print(df.head(n))


def save_to_excel(df, file_name, sheet_name):
    df.to_excel(file_name, sheet_name=sheet_name, index=False)


titanic = pd.read_csv("data/titanic.csv")

save_to_excel(titanic, 'titanic.xlsx', 'passengers')
