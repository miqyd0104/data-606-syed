def transform_movies(movies):
    transformed_movies = []

    for movie in movies:
        year = movie["startYear"]

        if year.isdigit():
            if movie["titleType"] == "movie" and int(year) >= 2010:
                selected_movie = {
                    "titleType": movie["titleType"],
                    "primaryTitle": movie["primaryTitle"],
                    "startYear": int(year),
                    "runtimeMinutes": movie["runtimeMinutes"],
                    "genres": movie["genres"]
                }

                transformed_movies.append(selected_movie)

    return transformed_movies