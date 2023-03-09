import logging
from typing import List

from requests import HTTPError, get, JSONDecodeError, Response
from DKC_API.private_file import HEADERS, BASE_URL, MASTER_KEY

# !!! don't change !!!
MATERIAL_NAME = 'material'
CERTIFICATES_NAME = 'certificates'
STOCK_NAME = 'stock'
RELATED_NAME = 'related'
VIDEO_NAME = 'video'
DRAWINGS_SKETCH_NAME = 'drawings_sketch'
DESCRIPTION_NAME = 'description'
ANALOGS_NAME = 'analogs'
SPECIFICATION_NAME = 'specification'


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
    return get(material_url, headers=HEADERS)


def get_material_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        '',
        'Get material'
    )


def get_certificates_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{CERTIFICATES_NAME}',
        f'Get material {CERTIFICATES_NAME}'
    )


def get_videos_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{VIDEO_NAME}',
        f'Get material {VIDEO_NAME}'
    )


def get_stock_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{STOCK_NAME}',
        f'Get material {STOCK_NAME}'
    )


def get_related_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{RELATED_NAME}',
        f'Get material {RELATED_NAME}'
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
        f'/{DESCRIPTION_NAME}',
        f'Get material {DESCRIPTION_NAME}'
    )


def get_analogs_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{ANALOGS_NAME}',
        f'Get material {ANALOGS_NAME}'
    )


def get_specification_response(material_code: str):
    return get_catalog_material_response(
        material_code,
        f'/{SPECIFICATION_NAME}',
        f'Get material {SPECIFICATION_NAME}'
    )


def create_material(material_response: Response, material_code: str):
    try:
        material_json = material_response.json() \
            .get(MATERIAL_NAME)
        material_certificates_json = get_certificates_response(material_code).json()
        material_stock_json = get_stock_response(material_code).json()
        material_related_json = get_related_response(material_code).json() \
            .get(RELATED_NAME).get(material_code)
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
        return {
            MATERIAL_NAME: material_json,
            CERTIFICATES_NAME: material_certificates_json,
            STOCK_NAME: material_stock_json,
            RELATED_NAME: material_related_json,
            VIDEO_NAME: material_videos_json,
            DRAWINGS_SKETCH_NAME: material_drawings_sketch_json,
            DESCRIPTION_NAME: material_description_json,
            ANALOGS_NAME: material_analogs_json,
            SPECIFICATION_NAME: material_specification_json,
        }
    except JSONDecodeError as err:
        print(err)
        logging.error(err)
    except AttributeError as err:
        print(f'Нет ответа по коду - \'{material_code}\'')
        logging.error(err)


def get_material_or_error(material_code: str):
    material_response = get_material_response(material_code)
    try:
        material_response.raise_for_status()
    except HTTPError as err:
        error_message = material_response.json().get("message")
        error = f'Ошибка по коду \'{material_code}\': ' \
                f'({material_response.status_code}) - {error_message}'
        logging.error(err)
        return error
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
            raise DkcAccessTokenError()
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(logging.INFO)
        handler = logging.FileHandler('dkc.log', 'w', self.base_encoding)
        self.root_logger.addHandler(handler)

    def __get_access_token(self):
        result = None
        print(self.AUTH_URL)
        if 'AccessToken' in HEADERS:  # delete if token exists
            del HEADERS['AccessToken']
        response = get(self.AUTH_URL, headers=HEADERS)
        print(f'access_token status_code={response.status_code}')
        try:
            response.raise_for_status()
            try:
                result = str(response.json().get('access_token'))
            except JSONDecodeError as err:
                logging.error(err)
        except HTTPError as err:
            logging.error(err)
        return result

    def get_materials(self, material_codes: List[str]):
        result = []
        for material_code in material_codes:
            material_or_error = get_material_or_error(material_code)
            if isinstance(material_or_error, dict):
                print(f'Материал с кодом \'{material_code}\' получен.')
                result.append(material_or_error)
            else:
                print(material_or_error)
                logging.info(material_or_error)
        logging.info(f'-' * 100)
        return result
