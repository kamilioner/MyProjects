import pandas as pd

### serach with more criteria ###

movies = pd.read_csv('imdb_1000.csv')

print(movies.loc[(movies['duration'] >= 200) & (movies['genre'].isin(['Crime', 'Drama', 'Action'])), 'genre'])


# or -> |
# and -> &




