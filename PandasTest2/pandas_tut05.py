import pandas as pd

### reading Series ###

ufo = pd.read_csv('ufo.csv')

ufo.drop('Colors Reported', axis=1, inplace=True)

print(ufo.head())

ufo.drop(['City', 'State'], axis=1, inplace=True)

print(ufo.head())

ufo.drop([0, 1], axis=0, inplace=True)

print(ufo.head())