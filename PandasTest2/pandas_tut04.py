import pandas as pd

### Changing column names ###

ufo = pd.read_csv('ufo.csv')

print(ufo.head())

ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)

print(ufo.head())

ufo_cols = ['city', 'color_reported', 'shape_reported', 'state', 'time']

ufo.columns = ufo_cols

print(ufo.columns)

ufo = pd.read_csv('ufo.csv')

ufo.columns = ufo.columns.str.replace(' ', '_')

print(ufo.columns)