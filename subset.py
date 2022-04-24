import pandas as pd
from pandas import Series


def print_head(series: Series):
    print(series.head())


#  A pandas Series is 1-dimensional and only the number of rows is returned.
def print_shape(series: Series):
    print(ages.shape)


titanic = pd.read_csv("data/titanic.csv")

# I’m interested in the age of the Titanic passengers.
ages = titanic["Age"]

print_shape(ages)
