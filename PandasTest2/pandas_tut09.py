import pandas as pd
import numpy as np

### Selecting particular colums/rows ###

# ufo = pd.read_csv('ufo.csv')

# print(ufo.columns)
#
# ufo = pd.read_csv('ufo.csv', usecols=[0, 4])
#
# print(ufo.columns)
#
# ufo = pd.read_csv('ufo.csv', nrows=3)
#
# print(ufo)

### print by index/print by iterration ###

# ufo = pd.read_csv('ufo.csv', nrows=3)
# for c in ufo.City:
#     print(c)
#
# for index, row in ufo.iterrows():
#     print(index, row.City, row.State)

### describe with include ###

drinks = pd.read_csv('drinks.csv')

print(drinks.dtypes)

print(drinks.select_dtypes(include=[np.number]).dtypes)

print(drinks.describe(include=['object', 'float64']))

print(drinks.describe(include=['object']))
