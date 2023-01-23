import logging
from collections import namedtuple
from json import JSONDecodeError
from typing import List

from requests import HTTPError, get

from material import Material
from private_file import HEADERS, BASE_URL, MASTER_KEY


def get_material_response(material_code: str):
    response = None
    material_url = f'{BASE_URL}/catalog/material?code={material_code}'
    logging.info(f'Get response from : {material_url}')
    try:
        response = get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return response


def create_material(material_object: dict) -> Material:
    # material_object.pop('sale') # test unpacking
    return Material(**material_object)


def custom_material_obj_decoder(material_object: dict):
    return namedtuple('X', material_object.keys())(*material_object.values())


class DkcObj:
    def __init__(self):
        self.base_encoding = 'UTF-8'
        self.AUTH_URL = f'{BASE_URL}/auth.access.token/{MASTER_KEY}'
        self.access_token = self.__get_access_token()
        logging.basicConfig(filename="dkc_log.txt", level=logging.DEBUG)

    def __get_access_token(self):
        result = None
        print(self.AUTH_URL)
        try:
            response = get(self.AUTH_URL, headers=HEADERS)
            if self.base_encoding.lower() != response.encoding.lower():
                self.base_encoding = response.encoding
            print(f'status_code={response.status_code}')
            try:
                response.raise_for_status()
                try:
                    result = response.json()['access_token']
                except JSONDecodeError as err:
                    print(err.args)
            except HTTPError as err:
                print(err.args)
        except Exception as err:
            logging.error(err.args)
        return result

    def get_materials(self, material_codes: List[str]) -> List[Material]:
        result = []
        for material_code in material_codes:
            material_response = get_material_response(material_code)

            print(material_response.content.decode('utf-8'))

            json_obj = None
            try:
                json_obj = material_response.json()
            except JSONDecodeError as err:
                print(err.args)

            if json_obj:
                material_obj = json_obj.get('material')
                material = create_material(material_obj)
                result.append(material)
        return result


if __name__ == '__main__':
    pass
