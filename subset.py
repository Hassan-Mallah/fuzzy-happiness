import pandas as pd
from pandas import DataFrame

titanic = pd.read_csv("data/titanic.csv")

# I’m interested in the age of the Titanic passengers.
ages = titanic["Age"]

print(ages.head())