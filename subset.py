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
# e.g. check_condition(subset['Age'], operator.gt, 10)
def check_condition(series: Series, operation, value) -> Series:
    return operation(series, value)


# filter_with_series(titanic, above_35)
def filter_with_series(df: DataFrame, series: Series):
    print(df[series])


# using isin(), to check whether elements in Series are contained in `values`
def filter_series_data(df: DataFrame, name, values: list):
    return df[df[name].isin(values)]


# return not null data for a series
def get_not_null(df: DataFrame, name):
    return df[df[name].notna()]


titanic = pd.read_csv("data/titanic.csv")

age_no_na = get_not_null(titanic, 'Age')

print(age_no_na)
