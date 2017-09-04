import pandas as pd

drinks = pd.read_csv('drinks.csv')

print(drinks.head())
print(drinks.info())

print(drinks.info(memory_usage='deep'))

print((drinks.memory_usage(deep=True)).sum())
print(sorted(drinks['continent'].unique()))

drinks['continent'] = drinks.continent.astype('category')

print(drinks.continent.head())
print(drinks['continent'].cat.codes.head())

print(drinks.memory_usage(deep=True))

df = pd.DataFrame({'ID':[100,101,102,103], 'quality':['good', 'very good', 'good', 'excellent']})
print(df)
print(df.sort_values('quality'))

df['quality'] = df['quality'].astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
print(df['quality'])

print(df.sort_values('quality'))

print(df.loc[df['quality'] > 'good', :])