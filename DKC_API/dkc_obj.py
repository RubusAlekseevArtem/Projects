import logging
from typing import List

from requests import HTTPError, get, JSONDecodeError, Response

SLEEP_DELAY = 0.1  # seconds


def get_catalog_material_response(
        material_code: str,
        catalog_path: str,
        log_info: str,
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
        # sleep(SLEEP_DELAY)
        return get(material_url, headers=HEADERS)
    except Exception as err:
        logging.error(err.args)
    return None


from .private_file import HEADERS, BASE_URL, MASTER_KEY


def get_material_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '',
        'Get material'
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


def get_related_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '/related',
        'Get material related'
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


def create_material(material_response: Response, material_code: str):
    """

    @param material_response:
    @param material_code:
    @return: None or dict material
    """
    try:
        material_json = material_response.json() \
            .get(MATERIAL_NAME)
        material_certificates_json = get_certificates_response(material_code).json()
        material_stock_json = get_stock_response(material_code).json()
        material_related_json = get_related_response(material_code).json() \
            .get(RELATED_NAME).get(material_code)
        material_accessories_json = get_accessories_response(material_code).json() \
            .get(ACCESSORIES_NAME).get(material_code)
        material_videos_json = get_videos_response(material_code).json() \
            .get(VIDEO_NAME).get(material_code)
        material_drawings_sketch_json = get_drawings_sketch_response(material_code).json() \
            .get(DRAWINGS_SKETCH_NAME).get(material_code)
        material_description_json = get_description_response(material_code).json() \
            .get(DESCRIPTION_NAME).get(material_code)
        material_analogs_json = get_analogs_response(material_code).json() \
            .get(ANALOGS_NAME).get(material_code)
        material_specification_json = get_specification_response(material_code).json() \
            .get(SPECIFICATION_NAME).get(material_code)
        material = {
            MATERIAL_NAME: material_json,
            CERTIFICATES_NAME: material_certificates_json,
            STOCK_NAME: material_stock_json,
            RELATED_NAME: material_related_json,
            ACCESSORIES_NAME: material_accessories_json,
            VIDEO_NAME: material_videos_json,
            DRAWINGS_SKETCH_NAME: material_drawings_sketch_json,
            DESCRIPTION_NAME: material_description_json,
            ANALOGS_NAME: material_analogs_json,
            SPECIFICATION_NAME: material_specification_json,
        }
    except JSONDecodeError as err:
        print(err.args)
        logging.error(err)
        return
    return material


class HttpResponseError(Exception):
    """Error when receiving a response"""

    def __init__(self):
        super().__init__(self.__doc__)


# !!! don't change !!!
MATERIAL_NAME = 'material'
CERTIFICATES_NAME = 'certificates'
STOCK_NAME = 'stock'
RELATED_NAME = 'related'
ACCESSORIES_NAME = 'accessories'
VIDEO_NAME = 'video'
DRAWINGS_SKETCH_NAME = 'drawings_sketch'
DESCRIPTION_NAME = 'description'
ANALOGS_NAME = 'analogs'
SPECIFICATION_NAME = 'specification'


def get_material(material_code: str):
    material_response = get_material_response(material_code)
    try:
        material_response.raise_for_status()
    except HTTPError as err:
        message = material_response.json().get("message")
        print(f'Ошибка по коду \'{material_code}\' - {material_response.status_code} {message}')
        logging.error(err)
        return  # return if bad status_cod
    return create_material(material_response, material_code)


class DkcAccessTokenError(Exception):
    """Error getting access token to DKC API"""

    def __init__(self):
        super().__init__(self.__doc__)


class DkcObj:

    def __init__(self):
        self.base_encoding = 'UTF-8'
        self.AUTH_URL = f'{BASE_URL}/auth.access.token/{MASTER_KEY}'
        self.access_token = self.__get_access_token()
        if self.access_token:  # if to get access_token
            HEADERS['AccessToken'] = self.access_token
        else:
            logging.error(DkcAccessTokenError.__doc__)
            raise DkcAccessTokenError()
        logging.basicConfig(filename="dkc.log", level=logging.INFO)

    def __get_access_token(self):
        result = None
        print(self.AUTH_URL)
        try:
            if 'AccessToken' in HEADERS:  # delete if token exists
                del HEADERS['AccessToken']
            response = get(self.AUTH_URL, headers=HEADERS)
            if self.base_encoding.lower() != response.encoding.lower():
                self.base_encoding = response.encoding
            print(f'access_token status_code={response.status_code}')
            try:
                response.raise_for_status()
                try:
                    result = str(response.json().get('access_token'))
                except JSONDecodeError as err:
                    logging.error(err)
            except HTTPError as err:
                logging.error(err)
        except Exception as err:
            logging.error(err)
        return result

    def get_materials(self, material_codes: List[str]):
        result = []
        for material_code in material_codes:
            material = get_material(material_code)
            if material:
                print(f'Запрос по товару - \'{material_code}\' получен.')
                result.append(material)
            else:
                logging.info(f'Material with material_code=\'{material_code}\' does not exist')
                print(f'Материал с кодом {material_code} не найден.')
        logging.info(f'-' * 100)
        return result
