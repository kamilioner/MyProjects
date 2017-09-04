import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

# print(movies['title'].sort_values()) #sorting a series

print(movies.sort_values('duration', ascending=False).head()) #sorting a data frame