import pandas as pd
import matplotlib.pyplot as plt

### Visualisation by specific column and group by column values ###

drinks = pd.read_csv('drinks.csv')

print(drinks.head())

print(drinks.beer_servings.mean())

print(drinks.groupby('continent').beer_servings.sum())

###### ^ Most usefull feature right here!!!

print(drinks.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean', 'sum']))

print(drinks.groupby('continent').sum())

print(drinks.groupby('continent').mean().plot(kind='bar'))

### writing chart to a file ###

plt.savefig('alco_mean_drink.png')

plt.show()