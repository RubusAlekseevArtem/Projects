import json
from json import JSONDecodeError

import requests
from requests import HTTPError

from private_file import base_url, headers

PRODUCTS_URL = f'{base_url}/api/products/'

if __name__ == '__main__':
    # Все запросы используют метод GET
    print(PRODUCTS_URL)
    response = requests.get(PRODUCTS_URL, headers=headers)
    print(response.status_code)
    # print(response.text)
    try:
        response.raise_for_status()

        try:
            print(json.dumps(dict(response.headers), indent=4))
            data = response.json()
            print(f'{data=}')
        except JSONDecodeError as err:
            print(err.args)

    except HTTPError as err:
        error = json.loads(response.text)['error']
        print(f"error_code={error['error_code']}")
        print(f"error_message={error['error_message']}")
