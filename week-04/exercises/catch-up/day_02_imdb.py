"""A validated IMDb ETL version, preserving the original exercise files."""
import csv
from pathlib import Path

COLUMNS = ['titleType', 'primaryTitle', 'startYear', 'runtimeMinutes', 'genres']


def extract_movies(filename):
    with open(filename, newline='', encoding='utf-8-sig') as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames or not set(COLUMNS).issubset(reader.fieldnames):
            raise ValueError('Input is missing required IMDb headings')
        records = list(reader)
        if any(None in row or any(value is None for value in row.values()) for row in records):
            raise ValueError('Input contains a row with the wrong number of fields')
        return records


def parse_year(value):
    if value in (None, '', r'\N'):
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def transform_movies(movies, minimum_year=2010):
    selected = []
    for movie in movies:
        year = parse_year(movie.get('startYear'))
        if movie.get('titleType') == 'movie' and year is not None and year >= minimum_year:
            row = {column: movie[column] for column in COLUMNS}
            row['startYear'] = year
            # Missing runtime stays missing; zero would invent a duration.
            row['runtimeMinutes'] = None if row['runtimeMinutes'] == r'\N' else row['runtimeMinutes']
            selected.append(row)
    return selected


def load_movies(filename, movies):
    with open(filename, 'w', newline='', encoding='utf-8') as target:
        writer = csv.DictWriter(target, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(movies)  # None becomes a blank CSV field.


def run_pipeline(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('Use a separate destination')
    records = extract_movies(source)
    selected = transform_movies(records)
    load_movies(destination, selected)
    return len(records), len(selected)


def main():
    folder = Path(__file__).parent
    output = folder / 'outputs'
    output.mkdir(exist_ok=True)
    try:
        before, after = run_pipeline(folder.parent / 'imdbtitles.csv', output / 'movies_2010_onwards.csv')
    except (OSError, ValueError, csv.Error) as error:
        raise SystemExit(f'Pipeline failed: {error}') from error
    print(f'Read {before} records; saved {after} movies')
    print('Output: outputs/movies_2010_onwards.csv')


if __name__ == '__main__':
    main()
