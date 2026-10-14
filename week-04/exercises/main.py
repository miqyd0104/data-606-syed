from extract import extract_movies
from transform import transform_movies
from load import load_movies


movies = extract_movies("imdbtitles.csv")

transformed_movies = transform_movies(movies)

load_movies("transformed_movies.csv", transformed_movies)

print("Original records:", len(movies))
print("Selected movies:", len(transformed_movies))
print("Saved to transformed_movies.csv")

print (movies)

print (type (movies))