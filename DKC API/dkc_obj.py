import logging
from json import JSONDecodeError
from typing import List

from requests import HTTPError, get

from material import Material, MaterialRecord, create_material_record
from private_file import HEADERS, BASE_URL, MASTER_KEY


def get_material_response(material_code: str):
    material_url = f'{BASE_URL}/catalog/material?code={material_code}'
    logging.info(f'Get material from : {material_url}')
    try:
        return get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return None


def get_certificates_response(material_code: str):
    material_url = f'{BASE_URL}/catalog/material/certificates?code={material_code}'
    logging.info(f'Get material certificates from : {material_url}')
    try:
        return get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return None


def get_videos_response(material_code: str):
    material_url = f'{BASE_URL}/catalog/material/video?code={material_code}'
    logging.info(f'Get material video response from : {material_url}')
    try:
        return get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return None


def get_material(material_code: str) -> MaterialRecord:
    material_response = get_material_response(material_code)
    material_certificates = get_certificates_response(material_code)
    material_videos = get_videos_response(material_code)
    try:
        material_json = material_response.json().get('material')
        material_certificates_json = material_certificates.json()
        material_videos_json = material_videos.json().get('video').get(material_code)
        # print(unescape(material_response.content.decode(material_response.encoding)))
        return create_material_record(material_json, material_certificates_json, material_videos_json)
    except JSONDecodeError as err:
        print(err.args)


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

    def get_materials(self, material_codes: List[str]) -> List[MaterialRecord]:
        result = []
        for material_code in material_codes:
            material = get_material(material_code)
            if isinstance(material, MaterialRecord):
                result.append(material)
        return result
