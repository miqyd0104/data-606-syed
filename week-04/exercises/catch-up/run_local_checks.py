"""Run local exercises, regression tests and every notebook cell in order."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys


def main():
    folder = Path(__file__).parent
    for script in ['day_01_python.py', 'day_01_oop.py', 'day_02_files_csv.py',
                   'day_02_imdb.py', 'day_03_json_api.py']:
        print(f'\nRUN {script}', flush=True)
        subprocess.run([sys.executable, str(folder / script)], check=True, cwd=folder)
    subprocess.run([sys.executable, '-m', 'pytest', '-q'], check=True, cwd=folder)
    for filename in ['day_05_numpy.ipynb', 'day_05_pandas_optional.ipynb']:
        notebook = json.loads((folder / filename).read_text(encoding='utf-8'))
        namespace = {'__name__': '__main__'}
        count = 0
        with contextlib.redirect_stdout(io.StringIO()):
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code':
                    exec(compile(''.join(cell['source']), filename, 'exec'), namespace)
                    count += 1
        print(f'PASS {filename}: {count} code cells, including assertions')
    print('\nALL LOCAL CHECKS PASSED. Northwind is checked separately against SQL Server.')


if __name__ == '__main__':
    main()
