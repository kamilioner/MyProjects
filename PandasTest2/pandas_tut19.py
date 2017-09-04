import pandas as pd

ufo = pd.read_csv('ufo.csv')

print(ufo.shape)
ufo.drop('City', axis=1, inplace=True) ### Drop column 'City'/// axis=1 is column
print(ufo.shape)
# ufo.dropna(how='any', inplace=True) ### Drop all rows containing an empty value
# print(ufo.shape)

print(ufo.tail())
print(ufo.fillna(method='ffill').tail())
