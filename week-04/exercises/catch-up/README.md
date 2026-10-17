# Week 4 exercises

[← Week 4](../../README.md) · [Original IMDb exercise](../)

Worked solutions for the activities recorded in the five week 4 session notes. The original IMDb files remain alongside this folder. These solutions use small functions, comments and examples so each step can be explained and repeated.

The original lambda/testing worksheets and full task-board datasets were not supplied. The corresponding examples cover the recorded requirements with illustrative data; they are not a claim of matching unseen questions. Watching a course, participating in interview practice, and producing personal coursework evidence remain separate activities.

## Open and run in PyCharm

1. Download or clone the repository, then open its folder in PyCharm.
2. Select the project's Python interpreter. Create a `.venv` if necessary.
3. Open PyCharm's Terminal, move into `week-04/exercises/catch-up`, and install the dependencies using that interpreter:

```bash
python -m pip install -r requirements.txt
```

If the Mac only recognises `python3`, use that command when creating the environment. In an activated environment, `python` should point to its interpreter. The database additionally needs Microsoft's SQL Server ODBC driver; pip installs the Python interface, not the database driver or SQL Server itself.

4. Open a script and choose **Run**, or run the commands below in the Terminal. **Use Terminal for the database scripts**, because an ordinary IDE Run console may echo password input. Scripts derive their data paths from their own location.
5. Open the notebooks in PyCharm if your edition supports them. Alternatively run `python -m notebook` from this folder and open them in the browser. Restart the kernel and run every cell in order.

## Activity map

| Day | Activity | Solution |
| --- | --- | --- |
| Monday | Even values in first five elements; initials/space positions; lists without duplicates; input validation | [day_01_python.py](day_01_python.py) |
| Monday | Divisors/factors, alphabet positions, ID/password arithmetic, prime checks, lambda/map/filter/sorting practice | [day_01_python.py](day_01_python.py) |
| Monday | All four OOP pillars in one staff-pay example | [day_01_oop.py](day_01_oop.py) |
| Monday–Tuesday | Calculator testing in unittest and pytest, including parameterisation and an exception assertion | [calculator.py](calculator.py), [unittest tests](tests/test_unittest.py), [pytest tests](tests/test_pytest.py) |
| Monday–Tuesday | Red–green–refactor demonstration | [day_02_tdd.py](day_02_tdd.py) |
| Tuesday | Read/write/append text, handle errors, select first name/last name/email from a CSV | [day_02_files_csv.py](day_02_files_csv.py), [sample users](data/user_details.csv) |
| Tuesday–Wednesday | IMDb extract/transform/load, inclusive 2010 boundary, missing-value policy and output checks | [day_02_imdb.py](day_02_imdb.py) |
| Wednesday | JSON string/file round trips and fetching JSON over HTTP | [day_03_json_api.py](day_03_json_api.py) |
| Wednesday–Thursday | REST/API study notes and recall questions | [API study](day_03_rest_api.md) |
| Thursday | Northwind connection, customer count, product query, column names, parameterised city query, all three fetch methods and cleanup | [day_04_northwind.py](day_04_northwind.py) |
| Thursday | Optional SQLAlchemy/pandas SQL-read extension | [day_04_sqlalchemy.py](day_04_sqlalchemy.py) |
| Friday | Required array shapes, scores, weather, store sales, random purchases, reshape/transpose, indexing and saving | [NumPy notebook](day_05_numpy.ipynb) |
| Friday | Optional Pandas research, DataFrame inspection, selection, adding data, CSV and missing values | [Pandas notebook](day_05_pandas_optional.ipynb), [Pandas notes](day_05_pandas_notes.md) |

## Run the local exercises

```bash
python day_01_python.py
python day_01_oop.py
python day_02_files_csv.py
python day_02_imdb.py
python day_03_json_api.py
python -m unittest discover -s tests -p test_unittest.py -v
python -m pytest -q
python day_02_tdd.py
```

Alternatively, run `python run_local_checks.py` to execute the local examples, tests and both notebooks' code cells together. This does not contact Northwind or an external API.

The TDD demonstration intentionally prints failing tests before the passing stages. It verifies that the sequence behaves as expected, then exits successfully. Ordinary regression tests should all pass.

Generated CSV/text/JSON files go into the ignored `outputs/` directory. The scripts regenerate them on each run. The IMDb source is the existing `../imdbtitles.csv`; the original source and output files are not overwritten.

### IMDb rules and checks

- Keep only `titleType == "movie"` and `startYear >= 2010`.
- Keep title type, primary title, start year, runtime and genres.
- Convert the year to an integer during transformation. CSV fields become strings when read again.
- Missing or invalid years are excluded. The IMDb `\N` missing-runtime marker becomes `None` in Python and a blank output field; it is not replaced with an invented zero.
- Re-running the same input replaces the generated output rather than appending duplicates.
- The supplied input produced **850 input records and 722 selected movies** during verification. Counts alone do not prove correctness; boundary and row-content checks are also included.

### JSON from an endpoint

Without arguments, the JSON script only performs local round trips. To try a real endpoint that you are authorised to access:

```bash
python day_03_json_api.py --url https://your-server.example/data.json
```

Replace the placeholder with a real JSON URL. Tests use simulated responses, so they do not claim that an external service was contacted.

## Connect to Northwind

First check the Python package and registered database drivers:

```bash
python day_04_northwind.py --check-drivers
```

For an existing local SQL Server container that publishes port 1433:

```bash
python day_04_northwind.py --server localhost,1433 --local-training-certificate
```

For the Windows Express demonstration with integrated authentication:

```powershell
python day_04_northwind.py --server 'localhost\SQLEXPRESS' --windows-auth --local-training-certificate
```

Use your actual server, database login and published port. `localhost` is only correct when Python connects to SQL Server exposed on that same computer. SQL Server must already be running and Northwind must already be imported. Windows integrated authentication is not the Mac/container SQL-login setup.

Passwords are entered privately at the Terminal prompt and are not stored in the source. The scripts refuse the password-echo fallback in an ordinary IDE Run console. The local-training-certificate flag skips certificate validation only for a controlled local training instance. Leave it out for a server with a valid trusted certificate. For a shared training server, use the connection/security settings provided by the trainer.

On Apple Silicon, `db_support.py` restarts the command once with a process-local library path pointing to the already-installed Homebrew OpenSSL libraries, if present. This resolves the library-discovery failure encountered during the local check without changing system settings. The local SQLAlchemy example can be run with `python day_04_sqlalchemy.py --local-training-certificate`; enter the hostname and port separately when prompted.

Repeat with `--city Berlin`, an unmatched city, and `--batch-size 1` or `--batch-size 5`. A zero batch size is rejected before connecting. The script reruns the same ordered city query before comparing each fetch method; fetching again without re-executing continues from the cursor's current position.

All included SQL is read-only. Editing a Python row does not update SQL Server; an explicit SQL write and the appropriate transaction handling would be a separate operation.

## Verification and remaining activities

See [verification.md](verification.md) for the actual checks and their limits. The Northwind queries and SQLAlchemy extension have been checked against the local training database. Use your own connection details when running them elsewhere.

The REST API course itself still needs to be watched/completed in its course platform. Additional task-board SQL/SQLAlchemy questions, the original worksheets and original NumPy numeric inputs need checking against that board. AI Fundamentals coursework may require screenshots, two recorded workflow runs or a team activity; consult the [coursework reference](../../../ai-fundamentals/README.md) for the actual requirements. No course completion or personal demonstration is asserted by adding these files.

For each solution, practise: explain its input and output; predict one result; change one requirement; run the checks; then rebuild a small version in a blank file.
