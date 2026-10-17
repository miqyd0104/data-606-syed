"""JSON conversions and a GET request; runs offline unless a URL is provided."""
import argparse
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch_json(url):
    if not url.startswith(('https://', 'http://')):
        raise ValueError('Use an HTTP or HTTPS URL')
    request = Request(url, headers={'Accept': 'application/json'})
    try:
        with urlopen(request, timeout=10) as response:
            return json.load(response)
    except HTTPError as error:
        raise RuntimeError(f'HTTP request failed with status {error.code}') from error
    except URLError as error:
        raise RuntimeError(f'Could not reach the server: {error.reason}') from error
    except TimeoutError as error:
        raise RuntimeError('The request timed out') from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError('The response was not valid readable JSON') from error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Optional endpoint returning JSON')
    args = parser.parse_args()
    car = {'name': 'Example car', 'electric': True, 'previous_owner': None}
    text = json.dumps(car)
    restored = json.loads(text)
    print('Python -> JSON text:', text)
    print('JSON text -> Python:', restored)
    folder = Path(__file__).parent / 'outputs'
    folder.mkdir(exist_ok=True)
    with (folder / 'car.json').open('w', encoding='utf-8') as target:
        json.dump(car, target, indent=2)
    with (folder / 'car.json').open(encoding='utf-8') as source:
        print('Read from JSON file:', json.load(source))
    if args.url:
        print('Response:', fetch_json(args.url))
    else:
        print('No external request made. Use --url to practise a live GET.')


if __name__ == '__main__':
    main()
