import csv


def load_movies(filename, movies):
    columns = [
        "titleType",
        "primaryTitle",
        "startYear",
        "runtimeMinutes",
        "genres"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(movies)


        # add try & accept
