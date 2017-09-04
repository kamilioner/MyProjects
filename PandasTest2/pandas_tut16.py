import pandas as pd

drinks = pd.read_csv('drinks.csv')

print(drinks.head())

print(drinks.index)

print(drinks[drinks.continent == 'South America'])
print()
print(drinks.loc[23, 'beer_servings'])
drinks.set_index('country', inplace=True)

print(drinks.head())

print(drinks.columns)
print()
print(drinks.loc['Brazil', 'beer_servings'])
drinks.index.name = None
print(drinks.head())

drinks.index.name = 'country'
drinks.reset_index(inplace=True)
print(drinks.head())

print(drinks.describe().index)

print(drinks.describe().loc['25%', 'beer_servings'])