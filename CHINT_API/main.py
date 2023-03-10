import json
import logging
from datetime import datetime
from json import JSONDecodeError

import requests
from requests import HTTPError

from .private_file import base_url, headers

PRODUCTS_URL = f'{base_url}/api/products/'
PRICES_URL = f'{base_url}/api/prices/'
PRODUCT_GROUPS_URL = f'{base_url}/api/product_groups/'
PRODUCT_PROPERTIES_URL = f'{base_url}/api/product_properties/'

RESULT_FILE_NAME = 'load_data.txt'
ENCODING = 'utf-8'

# don't change!
SUCCESS_KEY = 'success'
ERROR_KEY = 'error'
ERROR_CODE_KEY = 'error_code'
ERROR_MESSAGE_KEY = 'error_message'
LIMIT = 25  # available -> [0, 25, 50, 100]


# class ProductGetValues(BaseGetValues):


def get_product(vendor_code, print_to_console=True):
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
    # if print_to_console:
    #     print(f'status_code={response.status_code}')
    # if print_to_console:
    #     print(json.dumps(dict(response.headers), indent=4)) # headers
    try:
        response.raise_for_status()
        try:
            json_resp = response.json()
            request_is_success = json_resp.get(SUCCESS_KEY)
            if request_is_success:
                if print_to_console:
                    print(f"{vendor_code} - получен")
                return json_resp
            else:
                error = json_resp[ERROR_KEY]
                if print_to_console:
                    print(f"{vendor_code} - (error_code={error[ERROR_CODE_KEY]}) {error[ERROR_MESSAGE_KEY]}")
        except JSONDecodeError as err:
            if print_to_console:
                print('Не удалось получить json из запроса')
                print(err)
            logging.error(err)
    except HTTPError:
        error = json.loads(response.text)[ERROR_KEY]
        if print_to_console:
            print(f"error_code={error[ERROR_CODE_KEY]}")
            print(f"error_message={error[ERROR_MESSAGE_KEY]}")
    return None


def get_products(vendor_codes, print_to_console=True):
    def create_product(product_json_obj):
        prod = product_json_obj.get('data').get('products')[0]
        # pprint.pprint(product)
        return prod

    result = []
    t1 = datetime.now()
    for vendor_code in vendor_codes:
        product = get_product(vendor_code, print_to_console)
        if product:
            result.append(create_product(product))
    t2 = datetime.now()
    result_time = t2 - t1
    print(f'result_time={result_time}')
    return result


if __name__ == '__main__':
    print(PRODUCTS_URL)
    # 521527
    # 521525
    # 521367
    # 521111
    codes = [521527, 521525, 521367, 521111]
    products = get_products(codes)
    json_data = json.dumps(
        products,
        indent=4,
        ensure_ascii=False)
    with open(RESULT_FILE_NAME, 'w', encoding=ENCODING) as f:
        f.writelines(json_data)

    # # цены берутся целиком
    # print(PRICES_URL)
    # response = requests.get(PRICES_URL, headers=headers)
    # try:
    #     response.raise_for_status()
    #     try:
    #         json_resp = response.json()
    #         request_is_success = json_resp.get(SUCCESS_KEY)
    #         if request_is_success:
    #             print(f'Получено: {json_resp.get("data").get("items_count")}')
    #             prices = json_resp.get('data').get('prices')
    #             json_data = json.dumps(
    #                 prices,
    #                 indent=4,
    #                 ensure_ascii=False)
    #             with open(RESULT_FILE_NAME, 'w', encoding=ENCODING) as f:
    #                 f.writelines(json_data)
    #         else:
    #             error = json_resp[ERROR_KEY]
    #             print(f"(error_code={error[ERROR_CODE_KEY]}) {error[ERROR_MESSAGE_KEY]}")
    #     except JSONDecodeError as err:
    #         print('Не удалось получить json из запроса')
    # except HTTPError:
    #     error = json.loads(response.text)[ERROR_KEY]
    #     print(f"error_code={error[ERROR_CODE_KEY]}")
    #     print(f"error_message={error[ERROR_MESSAGE_KEY]}")

    # # список категорий продуктов берется целиком
    # print(PRODUCT_GROUPS_URL)
    # response = requests.get(PRODUCT_GROUPS_URL, headers=headers)
    # try:
    #     response.raise_for_status()
    #     try:
    #         json_resp = response.json()
    #         request_is_success = json_resp.get(SUCCESS_KEY)
    #         if request_is_success:
    #             print(f'Получено: {json_resp.get("data").get("product_groups_count")}')
    #             product_groups = json_resp.get('data').get('product_groups')
    #             json_data = json.dumps(
    #                 product_groups,
    #                 indent=4,
    #                 ensure_ascii=False)
    #             with open(RESULT_FILE_NAME, 'w', encoding=ENCODING) as f:
    #                 f.writelines(json_data)
    #         else:
    #             error = json_resp[ERROR_KEY]
    #             print(f"(error_code={error[ERROR_CODE_KEY]}) {error[ERROR_MESSAGE_KEY]}")
    #     except JSONDecodeError as err:
    #         print('Не удалось получить json из запроса')
    # except HTTPError:
    #     error = json.loads(response.text)[ERROR_KEY]
    #     print(f"error_code={error[ERROR_CODE_KEY]}")
    #     print(f"error_message={error[ERROR_MESSAGE_KEY]}")

    # # список параметров продуктов берется целиком
    # print(PRODUCT_PROPERTIES_URL)
    # response = requests.get(PRODUCT_PROPERTIES_URL, headers=headers)
    # try:
    #     response.raise_for_status()
    #     try:
    #         json_resp = response.json()
    #         request_is_success = json_resp.get(SUCCESS_KEY)
    #         if request_is_success:
    #             print(f'Получено: {json_resp.get("data").get("properties_count")}')
    #             products_properties = json_resp.get('data').get('properties')
    #             json_data = json.dumps(
    #                 products_properties,
    #                 indent=4,
    #                 ensure_ascii=False)
    #             with open(RESULT_FILE_NAME, 'w', encoding=ENCODING) as f:
    #                 f.writelines(json_data)
    #         else:
    #             error = json_resp[ERROR_KEY]
    #             print(f"(error_code={error[ERROR_CODE_KEY]}) {error[ERROR_MESSAGE_KEY]}")
    #     except JSONDecodeError as err:
    #         print('Не удалось получить json из запроса')
    # except HTTPError:
    #     error = json.loads(response.text)[ERROR_KEY]
    #     print(f"error_code={error[ERROR_CODE_KEY]}")
    #     print(f"error_message={error[ERROR_MESSAGE_KEY]}")
