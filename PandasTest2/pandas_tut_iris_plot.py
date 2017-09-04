import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('IRIS.csv', header=None, usecols=[0, 2, 4, 6, 8], names=['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Flower_name' ])

print(iris.head())

iris.groupby('Flower_name',).mean().plot(kind='bar')
plt.show()