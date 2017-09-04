import pandas as pd

### Sum by specific continent ###

drinks = pd.read_csv('drinks.csv')

# print(drinks.head())

# print(drinks.drop('continent', axis=1).head())

print(drinks[drinks['continent'] == 'Europe'].sum())