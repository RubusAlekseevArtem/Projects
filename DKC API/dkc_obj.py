import logging
from json import JSONDecodeError
from typing import List

from requests import HTTPError, get

from material import MaterialRecord, create_material_record
from private_file import HEADERS, BASE_URL, MASTER_KEY


def get_catalog_material_response(
        material_code: str,
        catalog_path: str = '',
        log_info: str = f'Get catalog material'
):
    """
    Запрос данных по материалу
    :param log_info:
    :param material_code: Код материала
    :param catalog_path: Путь к запросам по материалу
    :return: Response or None
    """
    material_url = f'{BASE_URL}/catalog/material{catalog_path}?code={material_code}'
    logging.info(f'{log_info} (from {material_url})')
    try:
        return get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return None


def get_material_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        log_info='Get material'
    )


def get_certificates_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/certificates',
        'Get material certificates'
    )


def get_videos_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/video',
        'Get material video'
    )


def get_stock_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/stock',
        'Get material stock'
    )


def get_accessories_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/accessories',
        'Get material accessories'
    )


def get_drawings_sketch_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/drawings/sketch',
        'Get material drawings sketch'
    )


def get_description_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/description',
        'Get material description'
    )


def get_analogs_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/analogs',
        'Get material analogs'
    )


def get_specification_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/specification',
        'Get material specification'
    )


def get_material(material_code: str) -> MaterialRecord:
    material_response = get_material_response(material_code)
    material_certificates = get_certificates_response(material_code)
    material_videos = get_videos_response(material_code)
    material_stock = get_stock_response(material_code)
    material_accessories = get_accessories_response(material_code)
    material_drawings_sketch = get_drawings_sketch_response(material_code)
    material_description = get_description_response(material_code)
    material_analogs = get_analogs_response(material_code)
    material_specification = get_specification_response(material_code)
    try:
        material_json = material_response.json().get('material')
        material_certificates_json = material_certificates.json()
        material_videos_json = material_videos.json().get('video').get(material_code)
        material_stock_json = material_stock.json()
        material_accessories_json = material_accessories.json().get('accessories').get(material_code)
        material_drawings_sketch_json = material_drawings_sketch.json().get('drawings_sketch').get(material_code)
        material_description_json = material_description.json().get('description').get(material_code)
        material_analogs_json = material_analogs.json().get('analogs').get(material_code)
        material_specification_json = material_specification.json().get('specification').get(material_code)
        return create_material_record(
            material_json,
            material_certificates_json,
            material_videos_json,
            material_stock_json,
            material_accessories_json,
            material_drawings_sketch_json,
            material_description_json,
            material_analogs_json,
            material_specification_json
        )
    except JSONDecodeError as err:
        print(err.args)
    return MaterialRecord()


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
