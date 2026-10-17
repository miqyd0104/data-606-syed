"""Read-only Northwind practice. Connection details are prompted, never saved."""
import argparse
from contextlib import closing
from db_support import prepare_odbc, sql_password


def odbc_value(value):
    return '{' + value.replace('}', '}}') + '}'


def connection_string(driver, server, username, password, windows_auth=False, local_certificate=False):
    settings = (f'DRIVER={odbc_value(driver)};SERVER={odbc_value(server)};'
                'DATABASE=Northwind;Encrypt=yes;'
                f'TrustServerCertificate={"yes" if local_certificate else "no"};')
    if windows_auth:
        return settings + 'Trusted_Connection=yes;'
    return settings + f'UID={odbc_value(username)};PWD={odbc_value(password)};'


def fetch_batches(cursor, size):
    if size < 1:
        raise ValueError('Batch size must be at least 1')
    while True:
        batch = cursor.fetchmany(size)
        if not batch:
            return
        yield from batch


def run_queries(cursor, city, batch_size):
    cursor.execute('SELECT @@VERSION;')
    print('SQL Server:', cursor.fetchone()[0])
    cursor.execute('SELECT COUNT(*) FROM dbo.Customers;')
    print('Total customers:', cursor.fetchone()[0])
    cursor.execute('SELECT TOP (5) ProductName, UnitPrice FROM dbo.Products ORDER BY ProductID;')
    print('Product columns:', [column[0] for column in cursor.description])
    products = cursor.fetchall()
    print('Collection type:', type(products).__name__)
    for row in products:
        print('Product:', row.ProductName, row.UnitPrice, 'row type:', type(row).__name__)
    query = ('SELECT CustomerID, CompanyName, City FROM dbo.Customers '
             'WHERE City = ? ORDER BY CustomerID;')
    cursor.execute(query, (city,))
    all_rows = [tuple(row) for row in cursor.fetchall()]
    cursor.execute(query, (city,))
    one_rows = []
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        one_rows.append(tuple(row))
    cursor.execute(query, (city,))
    batch_rows = [tuple(row) for row in fetch_batches(cursor, batch_size)]
    if not (all_rows == one_rows == batch_rows):
        raise RuntimeError('Fetch results differed; check whether source data changed')
    print(f'All three fetch methods returned the same {len(all_rows)} rows for {city!r}')
    for row in batch_rows:
        print(row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-drivers', action='store_true')
    parser.add_argument('--server', help='Use the server/port from your working SQL client')
    parser.add_argument('--driver', default='ODBC Driver 18 for SQL Server')
    parser.add_argument('--windows-auth', action='store_true')
    parser.add_argument('--local-training-certificate', action='store_true',
                        help='Only for a controlled local training database with a self-signed certificate')
    parser.add_argument('--city', default='London')
    parser.add_argument('--batch-size', type=int, default=5)
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error('--batch-size must be at least 1')
    prepare_odbc()
    try:
        import pyodbc
    except ImportError:
        parser.exit(1, 'Install pyodbc into the interpreter running this file first.\n')
    drivers = pyodbc.drivers()
    if args.check_drivers:
        print('Registered ODBC drivers:', drivers)
        return
    if args.driver not in drivers:
        parser.error(f'Driver is unavailable. Installed drivers: {drivers}')
    server = args.server or input('SQL server (host,port or Windows instance): ').strip()
    username = '' if args.windows_auth else input('SQL username: ').strip()
    try:
        password = '' if args.windows_auth else sql_password()
    except RuntimeError as error:
        parser.exit(1, f'{error}\n')
    settings = connection_string(args.driver, server, username, password,
                                 args.windows_auth, args.local_training_certificate)
    try:
        with closing(pyodbc.connect(settings, timeout=5)) as connection:
            with closing(connection.cursor()) as cursor:
                run_queries(cursor, args.city, args.batch_size)
    except pyodbc.Error:
        # Avoid echoing a connection string or credentials into logs/screenshots.
        parser.exit(1, 'Connection/query failed. Check driver, server, login, certificate and Northwind setup.\n')


if __name__ == '__main__':
    main()
