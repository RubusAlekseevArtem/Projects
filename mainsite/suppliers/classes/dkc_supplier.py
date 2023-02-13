import os.path
import pprint
import sys

from .base_supplier import BaseSupplier
from .hierarchical_tree import IdCounter
from ..models import Supplier

sys.path.append(os.path.abspath(rf'..'))

from DKC_API.main import get_materials, DkcObj, DkcAccessTokenError


class DKCSupplier(BaseSupplier):
    def __init__(self, name: str = 'DKC API', pk=None):
        # trying to get id from db
        supplier = Supplier.objects.all().filter(name=name)
        if supplier:
            pk = supplier[0].pk
        super().__init__(name, pk)

    def __str__(self):
        return f'DKCSupplier({super().__str__()})'

    def get_tree_view_parameters(self) -> dict:
        id_counter = IdCounter()
        hierarchical_tree = {
            'Number': id_counter.id,
            'Name': "Материал DKC",
            'Children': [
                {
                    'Number': id_counter.id,
                    'Name': "Материал",
                    'FieldName': "material",
                    'Children': [
                        {
                            'Number': id_counter.id,
                            'Name': "Информация по материалу",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Фото материала",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Атрибуты материала",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "ETIM атрибуты материала",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Фасовка",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Средняя доставка",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Аксессуары",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Коды аксессуаров",
                        },
                        {
                            'Number': id_counter.id,
                            'Name': "Скидка",
                        },
                    ]
                },
                {
                    'Number': id_counter.id,
                    'Name': "Сертификаты материала",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Остатки на складах",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Сопутствующие материалы",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Аксессуары материала",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Видео",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Эскизы чертежей",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Описание",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Аналоги",
                },
                {
                    'Number': id_counter.id,
                    'Name': "Пересчет спецификации",
                },
            ]
        }
        return hierarchical_tree

    def get_data_from_api_with_parameters(self, params: dict):
        """
        Получение данных от DKC API
        @param parameters:
        @return:
        """
        material_codes = params.get('material_codes')
        # print(f'{params=}')
        # print(f'{material_codes=}')
        if material_codes:
            dkc = None  # create dkc obj for all materials responses
            try:
                dkc = DkcObj()
            except DkcAccessTokenError as err:
                print(err)
            return get_materials(material_codes, dkc)
        return None

    def get_supplier_parameters_from_api(self) -> tuple:
        material_codes = ['4400003']
        materials = get_materials(material_codes)
        for material in materials:
            keys = tuple(material.__dict__.keys())
        # print(keys)
        return keys
