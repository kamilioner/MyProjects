import pandas as pd

### search with criteria ###

movies = pd.read_csv('imdb_1000.csv')

# print(movies['title'].sort_values()) #sorting a series

#print(movies.head())

# print(movies.sort_values('duration', ascending=False).head()) #sorting a data frame
#
# print(movies.shape)
#
# booleans = []
#
# for length in movies['duration']:
#     if length >= 200:
#         booleans.append(True)
#     else:
#         booleans.append(False)
#
# print(booleans[0:5])
#
# print(len(booleans))
#
# is_long = pd.Series(booleans)
#
# print(is_long.head())
#
# print(movies[is_long])
#
# is_long = movies.duration >= 200
#
# print(is_long.head())
#
# print(movies[is_long])

#print(movies[movies['duration'] >= 200])

print(movies.loc[movies['duration'] >= 200, 'genre'])
