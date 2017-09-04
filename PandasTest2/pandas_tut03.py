import pandas as pd

### Dataframe type, describe, shape, dtype ###

movies = pd.read_csv('imdb_1000.csv')

print(movies.head())
print(movies.describe())
print(movies.shape)
print(movies.dtypes)
print(type(movies))

print(movies.describe(include=['object']))

