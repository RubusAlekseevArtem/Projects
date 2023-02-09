import logging
from json import JSONDecodeError
from typing import List

from requests import HTTPError, get

from .data_classes.certificate import Certificate
from .data_classes.material import Material
from .data_classes.stock import Stock
from .data_classes.video import Video
from .material import MaterialRecord

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


def create_material_record(
        material: dict,
        material_certificates: List[dict],
        material_videos: List[dict],
        material_stock: dict,
        material_related: List[str],
        material_accessories: List[str],
        material_drawings_sketch: List[str],
        material_description: List[str],
        material_analogs: List[str],
        material_specification: List[str],
) -> MaterialRecord:
    # material_data.pop('sale') # test unpacking
    record = MaterialRecord()

    record.material = Material(**material)
    record.certificates = [Certificate(**material_certificate) for material_certificate in material_certificates]
    record.videos = [Video(**material_video) for material_video in material_videos]
    record.stock = Stock(**material_stock)
    record.related = material_related
    record.accessories = material_accessories
    record.drawings_sketch = material_drawings_sketch
    record.description = material_description
    record.analogs = material_analogs
    record.specification = material_specification

    return record


def add_data_by_params(material_code: str, result_object: dict, params: dict):
    # for adaptive creating object
    # def get_func_by_parameter_name(parameter: str) -> Callable[[str], Response] | None:
    #     # material_json = get_material_response(material_code).json() \
    #     #     .get('material')
    #     # material_certificates_json = get_certificates_response(material_code).json()
    #     # material_videos_json = get_videos_response(material_code).json() \
    #     #     .get('video').get(material_code)
    #     # material_stock_json = get_stock_response(material_code).json()
    #     # material_related_json = get_related_response(material_code).json() \
    #     #     .get('related').get(material_code)
    #     # material_accessories_json = get_accessories_response(material_code).json() \
    #     #     .get('accessories').get(material_code)
    #     # material_drawings_sketch_json = get_drawings_sketch_response(material_code).json() \
    #     #     .get('drawings_sketch').get(material_code)
    #     # material_description_json = get_description_response(material_code).json() \
    #     #     .get('description').get(material_code)
    #     # material_analogs_json = get_analogs_response(material_code).json() \
    #     #     .get('analogs').get(material_code)
    #     # material_specification_json = get_specification_response(material_code).json() \
    #     #     .get('specification').get(material_code)
    #     match parameter:
    #         case "200":
    #             return
    #         case "404":
    #             print("Not Found")
    #         case "418":
    #             print("I'm a teapot")
    #         case _:
    #             return None
    #     # ['description', 'analogs', 'related', 'material', 'certificates',
    #     # 'videos', 'specification', 'drawings_sketch', 'accessories', 'stock']
    #
    # def get_object_from_response_by_parameter_name(
    #         material_code: str,
    #         response: Response,
    #         parameter: str):
    #     pass
    #
    # # print('add_data_by_params')
    # print(result_object)
    # print(params)
    #
    # suppliers_parameters = params.get('suppliers_parameters')
    #
    # if suppliers_parameters:
    #     for parameter in suppliers_parameters:  # перебор параметров
    #         func = get_func_by_parameter_name(parameter)  # получение функции для запроса
    #         if func:
    #             # получение результата из запроса
    #             response = func(material_code)
    #             # получение объекта из ответа
    #             data = get_object_from_response_by_parameter_name(material_code, response, parameter)
    #             # добавить полученный объект по ключу parameter
    #             result_object[parameter] = data

    # print('add_data_by_params')
    # print(result_object)
    # print(params)

    suppliers_parameters = params.get('suppliers_parameters')
    # print(suppliers_parameters)
    if suppliers_parameters:
        for parameter in suppliers_parameters:  # перебор параметров
            data = None
            match parameter:
                case 'material':
                    data = get_material_response(material_code).json().get('material')
                case 'certificates':
                    data = get_certificates_response(material_code).json()
                case 'videos':
                    data = get_videos_response(material_code).json().get('video').get(material_code)
                case 'stock':
                    data = get_stock_response(material_code).json()
                case 'related':
                    data = get_related_response(material_code).json().get('related').get(material_code)
                case 'accessories':
                    get_accessories_response(material_code).json().get('accessories').get(material_code)
                case 'drawings_sketch':
                    data = get_drawings_sketch_response(material_code).json().get('drawings_sketch').get(material_code)
                case 'description':
                    data = get_description_response(material_code).json().get('description').get(material_code)
                case 'analogs':
                    data = get_analogs_response(material_code).json().get('analogs').get(material_code)
                case 'specification':
                    data = get_specification_response(material_code).json().get('specification').get(material_code)
            # print(f'{parameter=} {data}')
            if data:
                # добавить полученный объект по ключу parameter
                # print(f'result_object[{parameter}] = {data}')
                result_object[parameter] = data


def get_material(material_code: str, params: dict = None):
    result_object = {}
    try:
        if params:
            add_data_by_params(material_code, result_object, params)
        else:
            material_json = get_material_response(material_code).json() \
                .get('material')
            material_certificates_json = get_certificates_response(material_code).json()
            material_videos_json = get_videos_response(material_code).json() \
                .get('video').get(material_code)
            material_stock_json = get_stock_response(material_code).json()
            material_related_json = get_related_response(material_code).json() \
                .get('related').get(material_code)
            material_accessories_json = get_accessories_response(material_code).json() \
                .get('accessories').get(material_code)
            material_drawings_sketch_json = get_drawings_sketch_response(material_code).json() \
                .get('drawings_sketch').get(material_code)
            material_description_json = get_description_response(material_code).json() \
                .get('description').get(material_code)
            material_analogs_json = get_analogs_response(material_code).json() \
                .get('analogs').get(material_code)
            material_specification_json = get_specification_response(material_code).json() \
                .get('specification').get(material_code)
            # return material by parameters in kwargs

            result_object = create_material_record(
                material_json,
                material_certificates_json,
                material_videos_json,
                material_stock_json,
                material_related_json,
                material_accessories_json,
                material_drawings_sketch_json,
                material_description_json,
                material_analogs_json,
                material_specification_json
            )
    except JSONDecodeError as err:
        print(err.args)
        logging.error(err)
    return result_object


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
            raise DkcAccessTokenError()  # raise error
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

    def get_materials(self, material_codes: List[str], params: dict = None):
        result = []
        for material_code in material_codes:
            material = get_material(material_code, params)
            if material:
                print(f'Запрос по товару - \'{material_code}\' получен.')
                result.append(material)
            else:
                logging.info(f'Material with material_code=\'{material_code}\' does not exist')
                print(f'Материал с кодом {material_code} не найден.')
        return result
