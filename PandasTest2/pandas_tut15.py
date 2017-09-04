import pandas as pd

ufo = pd.read_csv('ufo.csv')

print(ufo.tail())

print(ufo.isnull().tail())
print(ufo.notnull().tail())

print('Number of NULL values:')

print(ufo.isnull().sum())

print(ufo[ufo.City.isnull()])

print(ufo.shape)
print(ufo.dropna(how='any', inplace=False).shape) #drop line if any value is NaN
print(ufo.dropna(how='all', inplace=False).shape) #drop line if all values are NaN
print(ufo.dropna(subset=['City', 'Shape Reported'], how='any', inplace=False).shape) #drop line if value is missing in column 'City' or 'Shape Reported'
print(ufo.dropna(subset=['City', 'Shape Reported'], how='all', inplace=False).shape) #drop line if value is missing in column 'City' and 'Shape Reported'

print(ufo['Shape Reported'].value_counts())

print(ufo['Shape Reported'].value_counts(dropna=False))

########## IMPORTANT! To change NaN values into something: ###########

ufo['Shape Reported'].fillna(value='VARIOUS') # ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True) <- Permament change in dataframe


