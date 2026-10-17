"""Small environment helpers shared by the database exercises."""
import os
from getpass import GetPassWarning, getpass
from pathlib import Path
import sys
import warnings


def prepare_odbc():
    # Some Apple Silicon setups do not find Homebrew's existing TLS libraries.
    # Restart this command once with its library path set before Python starts.
    # This affects only this process; no system settings are changed.
    folder = Path('/opt/homebrew/opt/openssl@3/lib')
    if sys.platform == 'darwin' and (folder / 'libssl.3.dylib').exists():
        existing = os.environ.get('DYLD_LIBRARY_PATH', '')
        if str(folder) not in existing.split(':'):
            environment = os.environ.copy()
            environment['DYLD_LIBRARY_PATH'] = str(folder) + (':' + existing if existing else '')
            os.execve(sys.executable, [sys.executable, *sys.argv], environment)


def sql_password():
    # PyCharm's ordinary Run console may echo getpass input. Refuse that fallback.
    with warnings.catch_warnings():
        warnings.simplefilter('error', GetPassWarning)
        try:
            return getpass('SQL password: ')
        except GetPassWarning as error:
            raise RuntimeError('Run this script in PyCharm Terminal so the password stays hidden.') from error
