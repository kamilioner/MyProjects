import pandas as pd

drinks = pd.read_csv('drinks.csv')

drinks.set_index('country', inplace=True)
print(drinks.head())

print(drinks.continent.head())

print(drinks.continent.value_counts())
print(drinks.continent.value_counts().values)

print(drinks.continent.value_counts()['Africa'])
print(drinks.continent.value_counts().sort_index())

people = pd.Series([30000, 85000], index=['Albania', 'Andorra'], name='population')
print(people)

### Lookup ###

print(drinks.beer_servings * people)

### Concatenation ###

print(pd.concat([drinks, people], axis=1).head())
