import json
import logging
from datetime import datetime
from json import JSONDecodeError

import requests
from requests import HTTPError, Response

from private_file import base_url, headers

PRODUCTS_URL = f'{base_url}/api/products/'
PRICES_URL = f'{base_url}/api/prices/'

RESULT_FILE_NAME = 'chint.log'
ENCODING = 'utf-8'

# don't change!
SUCCESS_KEY = 'success'
ERROR_KEY = 'error'
ERROR_CODE_KEY = 'error_code'
ERROR_MESSAGE_KEY = 'error_message'
LIMIT = 25  # available -> [0, 25, 50, 100]


# Все запросы используют метод GET

def get_product(vendor_code):
    def get_json_or_none(response: Response):
        try:
            return response.json()
        except JSONDecodeError as err:
            print(err)
            logging.error(err)
        return None

    params = {
        'limit': LIMIT,
        'vendor_code': vendor_code,
        # 'page': '',
        # 'etim': '',
        # 'properties': '',
        # 'etim_properties': '',
        # 'xml': 0, # default 0 == not xml result format
    }
    response = requests.get(PRODUCTS_URL, headers=headers, params=params)
    # print(f'status_code={response.status_code}')
    # print(json.dumps(dict(response.headers), indent=4)) # headers
    try:
        response.raise_for_status()
        json_data = get_json_or_none(response)
        if json_data:
            request_is_success = json_data.get(SUCCESS_KEY)
            if request_is_success:
                print(f"{vendor_code} - получен")
                return json_data
            else:
                error = json_data[ERROR_KEY]
                print(f"{vendor_code} - (error_code={error[ERROR_CODE_KEY]}) {error[ERROR_MESSAGE_KEY]}")
        else:
            print('Не удалось получить json из запроса')
    except HTTPError:
        error = json.loads(response.text)[ERROR_KEY]
        print(f"error_code={error[ERROR_CODE_KEY]}")
        print(f"error_message={error[ERROR_MESSAGE_KEY]}")
    return None


def get_products(vendor_codes, print_result_time=True):
    result = []
    t1 = datetime.now()
    for vendor_code in vendor_codes:
        product = get_product(vendor_code)
        if product:
            result.append(product)
    t2 = datetime.now()
    if print_result_time:
        result_time = t2 - t1
        print(f'result_time={result_time}')
    return result


if __name__ == '__main__':
    print(PRODUCTS_URL)
    codes = [521527, 521525, 521367, 521111]
    products = get_products(codes)
    print(len(products))
