"""Optional extension: read Northwind into pandas through SQLAlchemy."""
import argparse
from db_support import prepare_odbc, sql_password


def read_products(server, port, username, password, local_certificate=False):
    prepare_odbc()
    import pandas as pd
    from sqlalchemy import URL, create_engine, text
    url = URL.create('mssql+pyodbc', username=username, password=password,
                     host=server, port=port, database='Northwind',
                     query={'driver': 'ODBC Driver 18 for SQL Server',
                            'Encrypt': 'yes',
                            'TrustServerCertificate': 'yes' if local_certificate else 'no'})
    engine = create_engine(url, hide_parameters=True)
    try:
        with engine.connect() as connection:
            frame = pd.read_sql_query(text('SELECT TOP (5) ProductName, UnitPrice '
                                           'FROM dbo.Products ORDER BY ProductID;'), connection)
            return frame
    finally:
        engine.dispose()


def main():
    prepare_odbc()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local-training-certificate', action='store_true')
    args = parser.parse_args()
    server = input('SQL server hostname: ').strip()
    port = int(input('Port [1433]: ').strip() or '1433')
    username = input('SQL username: ').strip()
    password = sql_password()
    print(read_products(server, port, username, password, args.local_training_certificate))


if __name__ == '__main__':
    main()
