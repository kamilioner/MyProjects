import pandas as pd
# import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

drinks = pd.read_csv('drinks.csv')

print(drinks)

print(pd.get_option('display.max_rows'))  # rows/columns

pd.set_option('display.max_rows', None)
pd.reset_option('display.max_rows')

train = pd.read_csv('titanic_train.csv')

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.precision', 2)

print(train.head())

# to display options (current and default)
pd.describe_option()

pd.reset_option('all')  # ignore errors here
