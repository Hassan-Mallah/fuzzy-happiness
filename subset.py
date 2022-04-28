import operator  # used for operator >, ==, !=, <, <=, ...
import pandas as pd
from pandas import Series, DataFrame


def print_head(series: Series):
    print(series.head())


#  A pandas Series is 1-dimensional and only the number of rows is returned.
def print_shape(series: Series):
    print(series.shape)


# I’m interested in the age of the Titanic passengers.
def get_series(df: DataFrame, name):
    return df[name]


# I’m interested in the age and sex of the Titanic passengers.
# e.g. get_subset(titanic, 'Age', 'Sex')
def get_subset(df: DataFrame, *args):
    columns = list(args)
    return df[columns]


def get_columns(df: DataFrame):
    print(df.columns)


# operator.gt is greater
def check_condition(series: Series, operation, value):
    print(operation(series, value))


titanic = pd.read_csv("data/titanic.csv")

subset = get_subset(titanic, 'Age', 'Sex')

check_condition(subset['Age'], operator.gt, 10)

