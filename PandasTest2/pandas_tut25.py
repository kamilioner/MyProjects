import pandas as pd
import numpy as np

movies = pd.read_csv('imdb_1000.csv')

print(movies.content_rating.isnull().sum())
print(movies[movies.content_rating.isnull()])

print(movies.content_rating.value_counts())

print(movies[movies.content_rating == 'NOT RATED'].content_rating)
# movies[movies.content_rating == 'NOT RATED'].content_rating = np.nan
# better way to do this:

movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan

print(movies.content_rating.isnull().sum())

# <- pandas must be sure that this is a copy!
top_movies = movies.loc[movies.star_rating >= 9, :].copy()

print(top_movies)

top_movies.loc[0, 'duration'] = 150
