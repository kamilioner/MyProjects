import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('imdb_1000.csv')

print(movies.head())
print(movies.dtypes)

print(movies['genre'].describe())

print(movies['genre'].value_counts())
print(movies['genre'].value_counts(normalize=True)) ### by percents ###

print(type(movies['genre'].value_counts(normalize=True)))

print(movies.genre.unique()) ### unique values ###
print(movies.genre.nunique()) ### unique values ###

print(pd.crosstab(movies.genre, movies.content_rating)) ### table of values by column

print(movies.duration.describe())
print(movies.duration.mean())

print(movies.duration.value_counts())

#movies.duration.plot(kind='hist')
movies.genre.value_counts().plot(kind='bar')

### values visualisation ###

plt.show()
