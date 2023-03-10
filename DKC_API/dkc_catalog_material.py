import logging
from timeit import timeit
from typing import List

from requests import HTTPError, get, JSONDecodeError, Response
from DKC_API.private_file import HEADERS, BASE_URL, AUTHORIZATION_URL

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
ACCESS_TOKEN_KEY = 'AccessToken'

ENCODING = 'UTF-8'
# строка формата сообщения
strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'
# строка формата времени
datefmt = '%Y-%m-%d %H:%M:%S'
# создаем форматтер

dkc_logger = logging.getLogger('dkc_logger')
dkc_logger.setLevel(logging.INFO)

handler = logging.FileHandler('dkc.log', 'w', ENCODING)
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
handler.setFormatter(formatter)

dkc_logger.addHandler(handler)


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
    url = f'{BASE_URL}/catalog/material{catalog_path}?code={material_code}'
    dkc_logger.info(f'{log_info} (from {url})')
    return get(url, headers=HEADERS)


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
        f'Get material {DRAWINGS_SKETCH_NAME}'
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
        dkc_logger.error(err)
    except AttributeError as err:
        print(f'Нет ответа по коду - \'{material_code}\'')
        dkc_logger.error(err)


def get_material_or_error(material_code: str):
    material_response = get_material_response(material_code)
    try:
        material_response.raise_for_status()
    except HTTPError:
        error_message = material_response.json().get('message')
        error = f'Ошибка по коду \'{material_code}\': ' \
                f'({material_response.status_code}) - {error_message}'
        return error
    return create_material(material_response, material_code)


def __get_dkc_access_token():
    result = None
    response = get(AUTHORIZATION_URL)
    try:
        response.raise_for_status()
        try:
            result = str(response.json().get('access_token'))
        except JSONDecodeError as err:
            dkc_logger.error(err)
    except HTTPError as err:
        dkc_logger.error(err)
    return result


def set_access_token_in_headers_or_raise(access_token=__get_dkc_access_token()):
    # if ACCESS_TOKEN_KEY in HEADERS:
    #     del HEADERS[ACCESS_TOKEN_KEY]
    if access_token:  # if to get access_token
        HEADERS[ACCESS_TOKEN_KEY] = access_token
    else:
        raise DkcErrorAccessToken()


def get_dkc_materials(material_codes: List[str], print_log=False):
    result_materials = []
    try:
        set_access_token_in_headers_or_raise()
        for material_code in material_codes:
            material_or_error = get_material_or_error(material_code)
            if isinstance(material_or_error, dict):
                if print_log:
                    print(f'Материал с кодом \'{material_code}\' получен.')
                result_materials.append(material_or_error)
            else:
                if print_log:
                    print(material_or_error)
                dkc_logger.info(material_or_error)
        dkc_logger.info(f'-' * 100)
    except DkcErrorAccessToken as err:
        dkc_logger.error(err)
    return result_materials


class DkcErrorAccessToken(Exception):
    """Error getting access token to DKC API"""

    def __init__(self):
        super().__init__(self.__doc__)


if __name__ == '__main__':
    codes = [
        '4400003',
        '4400013',
        'R5ST0231',
        '4400003',
        '4400013',
        'R5ST0231',
        '4400003',
        '4400013',
        'R5ST0231',
        '4400003',
    ]
    num = 10
    execute_time = timeit('get_materials(codes, False)', globals=globals(), number=num)
    print(f'codes_len={len(codes)} num={num} execute_time={execute_time} avg={execute_time / num}')
    # codes_len=10 num=1 execute_time=29.72600089944899 avg=29.72600089944899
    # codes_len=10 num=10 execute_time=278.3641758998856 avg=27.83641758998856
