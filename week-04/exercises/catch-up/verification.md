# Verification

[← Exercise guide](README.md)

Checked on 17 October 2026. This records execution results; course-platform participation is tracked separately.

## Local Python and notebooks

- The project opened in PyCharm with its local Python 3.12 environment selected. The local-check runner also passed inside PyCharm Terminal: examples, 19 tests plus 17 subtests, and both notebooks' code cells.
- `python -m pytest -q`: **19 passed, 17 subtests passed**.
- `python -m unittest discover -s tests -p test_unittest.py -v`: **14 tests passed** (the same core behaviours through unittest).
- Python, OOP, files/CSV, IMDb and local JSON demonstration scripts ran successfully.
- IMDb: **850 source records → 722 selected movies**. Tests also covered the 2009/2010 boundary, non-movie exclusion, missing/invalid years, missing runtimes, unchanged input, reruns, an empty CSV, a missing file and a separate output path.
- User-details CSV: **3 sample users** written with first name, last name and email. Quoted commas and invalid headings were checked separately.
- NumPy notebook: **8 code cells** executed in order, including shape, summary, filtering, axis, random-range, reshape/transpose and save/load assertions.
- Optional Pandas notebook: **3 code cells** executed in order, including DataFrame and missing-value assertions.
- Notebook cells were executed as Python source in fresh namespaces for each notebook; saved outputs are included. The local-check runner repeats those checks without requiring a running notebook server.
- TDD demonstration: verified the intentional **red → red → green → green** sequence. Expected failures in that demonstration are not regression-suite failures.
- JSON HTTP parsing was tested with simulated valid and invalid responses. A live public API/course endpoint was not used.

## Live Northwind checks

The existing local SQL Server container was started through Docker and accessed with the supplied training login. The password was entered at a private terminal prompt and was not saved in source files or this report. Queries were read-only.

| Check | Observed result |
| --- | --- |
| Registered driver | ODBC Driver 18 for SQL Server |
| Server connection/version query | SQL Server 2022 Express responded |
| Customer count | 91 |
| Product query and headings | Five rows; `ProductName` and `UnitPrice` |
| London, batch size 5 | 6 rows; all three fetch methods agreed |
| Berlin, batch size 1 | 1 row; all three fetch methods agreed |
| Unmatched test city | 0 rows; all three fetch methods agreed |
| Cursor continuation | First 10 + remaining 81 = 91 unique customer IDs |
| SQLAlchemy → Pandas | Five product rows and two columns; first product Chai |

A macOS OpenSSL discovery failure was resolved by supplying the installed Homebrew OpenSSL library directory to the Python process. The final helper performs this process-local setup automatically and was verified in a fresh process without manually setting the environment variable. It does not install libraries or change system settings.

## Coverage limits

The original lambda/testing worksheets, all task-board SQL extension questions and complete NumPy datasets were not available. Examples therefore implement the activities described in the session notes with sample data where needed. Exact worksheet parity must be checked against those originals.

The assigned REST API course still requires participation in its platform. Interview practice, team work and AI coursework recordings/screenshots cannot be established by running these scripts. See the existing course notes for those requirements.
