import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.DataFrame({'id': [100, 101, 102], 'color': ['red', 'blue', 'red']}, columns=['id', 'color'], index=['a', 'b', 'c'])
print(df)

df2 = pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color'])

arr = np.random.rand(4, 2)
print(arr)

df3 = pd.DataFrame(arr, columns=['one', 'two'])
print(df3)

df4 = pd.DataFrame({'student': np.arange(100, 110, 1), 'test': np.random.randint(60, 101, 10)})
print(df4)

s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')

print(pd.concat([df, s], axis=1)) ### to add vertical /// axis = 0 to concatenate at the end horizontal

