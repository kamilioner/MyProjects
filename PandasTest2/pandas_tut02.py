import pandas as pd

### Adding a series to a dataframe. ###

ufo = pd.read_csv('ufo.csv')
print(type(ufo))
print(ufo.head())

print(ufo['City'].head())
print(type(ufo['City']))

ufo['Location'] = ufo['City'] + ', ' + ufo['State']

print(ufo.head())
