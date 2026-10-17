import csv
from decimal import Decimal
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from calculator import add, subtract, divide
from day_01_python import (even_in_first_five, name_lists, lists_without_duplicates,
                           parse_over_100, ask_over_100, divisors, is_factor,
                           alphabet_position, id_generator, exercise_password, is_prime)
from day_01_oop import SalariedEmployee, HourlyEmployee, payroll
from day_02_files_csv import transform_users, HEADERS
from day_02_imdb import run_pipeline, transform_movies, COLUMNS
from day_03_json_api import fetch_json
from day_04_northwind import fetch_batches, connection_string


class PythonTests(unittest.TestCase):
    def test_limit_is_input_elements(self):
        self.assertEqual(even_in_first_five([1, 3, 5, 7, 2, 4, 6]), [2])

    def test_names(self):
        self.assertEqual(name_lists(['Ada Lovelace']), (['A'], [3], ['AL']))
        with self.assertRaises(ValueError):
            name_lists(['Ada'])

    def test_duplicates(self):
        self.assertEqual(lists_without_duplicates([[1, 2], [1, 1], []]), [[1, 2], []])

    def test_input_boundaries_and_retry(self):
        for invalid in ['100', '-101', '101.5', 'hello', '']:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                parse_over_100(invalid)
        self.assertEqual(parse_over_100(' 101 '), 101)
        responses = iter(['100', 'x', '102'])
        messages = []
        self.assertEqual(ask_over_100(lambda prompt: next(responses), messages.append), 102)
        self.assertEqual(len(messages), 2)

    def test_functions(self):
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertTrue(is_factor(36, 9))
        self.assertFalse(is_factor(9, 7))
        self.assertEqual(alphabet_position('T'), 19)
        self.assertEqual(id_generator('Bob'), '1141')
        self.assertEqual(exercise_password('Bob'), 1134)
        for invalid in ['', '!', 'ab']:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                alphabet_position(invalid)
        for number, expected in [(-1, False), (0, False), (1, False), (2, True), (9, False), (101, True)]:
            with self.subTest(number=number):
                self.assertEqual(is_prime(number), expected)

    def test_payroll_and_validation(self):
        result = payroll([SalariedEmployee('Ada', 36000), HourlyEmployee('Alan', 20, 120)])
        self.assertEqual(result, [('Ada', Decimal('3000.00')), ('Alan', Decimal('2400.00'))])
        with self.assertRaises(ValueError):
            SalariedEmployee('Ada', -1)


class CalculatorTests(unittest.TestCase):
    def test_arithmetic(self):
        for first, second, expected in [(1, 1, 2), (1, 2, 3), (-2, 2, 0)]:
            with self.subTest(first=first, second=second):
                self.assertEqual(add(first, second), expected)
        self.assertEqual(subtract(7, 2), 5)
        self.assertEqual(divide(6, 2), 3)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


class PipelineTests(unittest.TestCase):
    def test_imdb_boundaries_missing_values_and_input_not_mutated(self):
        def movie(year, kind='movie'):
            return dict(zip(COLUMNS, [kind, 'Example', year, r'\N', 'Drama']))
        records = [movie('2009'), movie('2010'), movie('2020', 'short'), movie(r'\N'), movie('bad')]
        selected = transform_movies(records)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]['startYear'], 2010)
        self.assertIsNone(selected[0]['runtimeMinutes'])
        self.assertEqual(records[1]['startYear'], '2010')

    def test_imdb_reruns_empty_and_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory)/'in.csv', Path(directory)/'out.csv'
            with source.open('w', newline='') as target:
                writer = csv.DictWriter(target, fieldnames=COLUMNS)
                writer.writeheader()
                writer.writerow(dict(zip(COLUMNS, ['movie', 'A, title', '2010', '90', 'Drama'])))
            self.assertEqual(run_pipeline(source, output), (1, 1))
            first_output = output.read_text()
            run_pipeline(source, output)
            self.assertEqual(output.read_text(), first_output)
            with self.assertRaises(ValueError):
                run_pipeline(source, source)
            with self.assertRaises(FileNotFoundError):
                run_pipeline(Path(directory)/'missing.csv', output)
            source.write_text(','.join(COLUMNS) + '\n')
            self.assertEqual(run_pipeline(source, output), (0, 0))
            self.assertEqual(output.read_text().strip(), ','.join(COLUMNS))

    def test_user_csv_quoted_field_and_bad_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory)/'users.csv', Path(directory)/'selected.csv'
            with source.open('w', newline='') as target:
                writer = csv.writer(target)
                writer.writerow(HEADERS)
                writer.writerow(['Dr', 'Ada', 'Lovelace, Byron', 'F', 'ada@example.com'])
            self.assertEqual(transform_users(source, output), 1)
            with output.open(newline='') as target:
                rows = list(csv.DictReader(target))
            self.assertEqual(rows[0]['last_name'], 'Lovelace, Byron')
            source.write_text('wrong,headers\n')
            with self.assertRaises(ValueError):
                transform_users(source, output)


class ApiAndDatabaseTests(unittest.TestCase):
    def test_json_response_and_invalid_json(self):
        # Mock HTTP responses: this checks parsing without a live internet call.
        with patch('day_03_json_api.urlopen', return_value=io.BytesIO(b'{"ok": true}')):
            self.assertEqual(fetch_json('https://example.com/data'), {'ok': True})
        with patch('day_03_json_api.urlopen', return_value=io.BytesIO(b'not json')):
            with self.assertRaises(ValueError):
                fetch_json('https://example.com/data')

    def test_batches_continue_and_stop(self):
        class FakeCursor:
            def __init__(self):
                self.remaining = list(range(13))
            def fetchmany(self, size):
                batch, self.remaining = self.remaining[:size], self.remaining[size:]
                return batch
        cursor = FakeCursor()
        self.assertEqual(list(fetch_batches(cursor, 5)), list(range(13)))
        self.assertEqual(list(fetch_batches(cursor, 5)), [])
        with self.assertRaises(ValueError):
            list(fetch_batches(cursor, 0))

    def test_odbc_quoting_and_certificate_default(self):
        settings = connection_string('Driver', 'host,1433', 'user', 'a;}b')
        self.assertIn('PWD={a;}}b};', settings)
        self.assertIn('TrustServerCertificate=no;', settings)


if __name__ == '__main__':
    unittest.main(verbosity=2)
