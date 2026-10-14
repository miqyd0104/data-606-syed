import csv


def extract_movies(filename):
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)