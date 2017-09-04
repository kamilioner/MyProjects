import pandas as pd

### how to read pandas documentation -> google: 'pandas function' ###
### API Reference -> All funtions I will ever need. ###
### What's new once in a while ###

### Top-Level meadns pd.function
ufo = pd.read_csv('ufo.csv')

pd.isnull(ufo).head()
### These are the same ###
ufo.isnull().head()

print(ufo.loc[0:4, :])
print(ufo.iloc[0:4, :])

### How to take a random sample

print(ufo.sample(n=5, random_state=42)) ### Random 5 rows by state

test = ufo.sample(frac=0.999, random_state=99)

print(ufo.loc[~ufo.index.isin(test.index), :])
