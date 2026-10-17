"""Read text, write/append orders and transform a user-details CSV."""
import csv
from pathlib import Path

HEADERS = ['title', 'first_name', 'last_name', 'gender', 'email']
SELECTED = ['first_name', 'last_name', 'email']


def read_order(filename):
    with open(filename, encoding='utf-8') as source:
        return [line.rstrip('\n') for line in source]


def transform_users(source_path, destination_path):
    source_path, destination_path = Path(source_path), Path(destination_path)
    if source_path.resolve() == destination_path.resolve():
        raise ValueError('Use a separate output file')
    with source_path.open(newline='', encoding='utf-8') as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != HEADERS:
            raise ValueError('Unexpected user-details headings')
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError('Expected five fields in each record')
            rows.append({key: row[key] for key in SELECTED})
    with destination_path.open('w', newline='', encoding='utf-8') as target:
        writer = csv.DictWriter(target, fieldnames=SELECTED)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main():
    folder = Path(__file__).parent
    output = folder / 'outputs'
    output.mkdir(exist_ok=True)
    order_path = output / 'order.txt'
    order_path.write_text('beans\n', encoding='utf-8')
    with order_path.open('a', encoding='utf-8') as target:
        target.write('carrots\n')
    print('Order:', read_order(order_path))
    count = transform_users(folder / 'data/user_details.csv', output / 'selected_users.csv')
    print(f'Saved {count} users to selected_users.csv')
    try:
        read_order(output / 'deliberately_missing.txt')
    except FileNotFoundError:
        print('Handled example: the requested file was not found')
    finally:
        print('File demonstration finished')


if __name__ == '__main__':
    main()
