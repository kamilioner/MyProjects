import pandas as pd
# import numpy as np
# import matplotlib as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

drinks = pd.read_csv('drinks.csv')
movies = pd.read_csv('imdb_1000.csv')
train = pd.read_csv('titanic_train.csv')
ufo = pd.read_csv('ufo.csv', parse_dates=['Time'])

# best way to use group by

print(drinks.head())
print(drinks.groupby('continent').beer_servings.max())

# multiple columns at once

print(drinks.groupby('continent').mean())

# append // concat
# concat is a top level (ps.concat) to concatenage rows

# merge / join
# merge is more general function

# pivot table !!!

# stact / unstack

print(drinks.groupby('continent').beer_servings.describe())
print(drinks.groupby('continent').beer_servings.describe().unstack())

# multiple indexes

df = pd.DataFrame({'name': ['A', 'A', 'B', 'B'], 'day': [1, 2, 1, 2],
                   'weight': [100, 103, 130, 129], 'height': [67, 68, 72, 72]})
print(df)

print(df.set_index(['name', 'day']))

# Identify outlayers ???

print(drinks.head())
# drinks.plot(kind='box')
# plt.pyplot.show()

print(movies.head())

print(movies[movies.duration >= 200])
# this is the same as
print(movies.loc[movies.duration >= 200, :])

print(movies[movies.duration >= 200].genre)
# it is adviced to do the second
print(movies.loc[movies.duration >= 200, 'genre'])

# learn panda string methods

# value counts

print(drinks.continent.value_counts())
a = drinks.continent.value_counts()
print()
print(drinks.continent.value_counts(normalize=True))
b = drinks.continent.value_counts(normalize=True)
print()
print(pd.concat([a, b], axis=1))
print()
print(drinks.sum(axis=0))
print()
print(drinks.sum(axis=1))
print()

# non-numerical to numerical

print(drinks.dtypes)
drinks['beer'] = drinks.beer_servings.astype(str)
print(drinks.head())
print(drinks.dtypes)

# v-lookup
print(movies.head())
mapping2 = pd.DataFrame({'ratings': ['R', 'PG-13'], 'kids': ['No', 'Yes']})
mapping2.set_index('ratings')
mapping = {'R': 'no', 'PG=13': 'yes', 'PG': 'yes'}
print(movies.content_rating.map(mapping))
print(pd.merge(movies, mapping2, left_on='content_rating', right_on='ratings'))

print(ufo.shape)
print(ufo.iloc[:-30, :].shape)

# datas - manipulation

print(ufo.dtypes)

ufo['year'] = ufo.Time.dt.year.astype(str)
ufo['month'] = ufo.Time.dt.month.astype(str).str.pad(width=2, fillchar='0')
ufo['new'] = ufo.year.str.cat(ufo.month, sep='-')
print(ufo.head())

# in staed of for

train['young_male'] = ((train.Sex == 'male') & (train.Age < 30)).map({True: 'Yes', False: 'No'})
print(train.head(10))

###
print()
print(train.Pclass.value_counts())

###

print(ufo.head())
print()
print(ufo.City.isnull().sum())
print()
print(ufo.loc[(ufo.City.isnull()) & (ufo["Colors Reported"] == 'RED'), "City"])
ufo.loc[(ufo.City.isnull()) & (ufo["Colors Reported"] == 'RED'), 'City'] = 'new_value'
# this will print nothing:
print(ufo.loc[(ufo.City.isnull()) & (ufo["Colors Reported"] == 'RED'), "City"])

# print(ufo.City.apply(len))

# visualisation: c-born / gg plot / matplotlib.plotlib

drinks2 = pd.read_csv('drinks.csv')
drinks3 = pd.read_csv('drinks.csv')
print((drinks3 != drinks2).sum())
drinks2.iloc[0, 0] = 'something else'
print((drinks3 != drinks2).sum())

print(drinks[drinks.continent.isin(['Asia', 'Africa'])])
print(drinks[~drinks.continent.isin(['Asia', 'Africa'])])

print(drinks.beer_servings.describe())
print(drinks.continent.describe())

print((drinks.continent == 'Asia').astype(int))

print(drinks[(drinks.continent == 'Africa') | (drinks.continent == 'Asia')])
# www.dataschool.io/talkpython
