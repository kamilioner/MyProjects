import pandas as pd
import matplotlib.pyplot as plt

ufo = pd.read_csv('ufo.csv')

print(ufo.head())

print(ufo.dtypes)

print(ufo.Time.str.slice(-5, -3).astype(int).head)

ufo['Time'] = pd.to_datetime(ufo.Time)

print(ufo.dtypes)

print(ufo.Time.dt.hour)
print(ufo.Time.dt.weekday_name)
print(ufo.Time.dt.dayofyear)

# working with time -> API REFERENCE ".dt."  <- time atributes

print(pd.to_datetime('1/1/1999'))
ts = pd.to_datetime('1/1/1999')

print(ufo.loc[ufo.Time >= ts, :])

print(ufo.Time.max())
print((ufo.Time.max() - ufo.Time.min()).days)

ufo['Year'] = ufo.Time.dt.year

ufo.Year.value_counts().sort_index().plot()

plt.show()
