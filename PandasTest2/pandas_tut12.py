import pandas as pd

### change a type ###

# drinks = pd.read_csv('drinks.csv')
#
# print(drinks.dtypes)
#
# drinks.beer_servings = drinks.beer_servings.astype(float)
#
# print(drinks.dtypes)

### To import Dataframe Series as specifiv type ###

# drinks = pd.read_csv('drinks.csv', dtype={'beer_servings':float})
#
# print(drinks.dtypes)

### Sum of strings ###

orders = pd.read_table('chipotle.tsv')

print(orders.head())

print(orders.dtypes)

print(orders.item_price.str.replace('$', '').astype(float).sum())

### to convert booleans(True/False) into integers I use .astype(int) ###


