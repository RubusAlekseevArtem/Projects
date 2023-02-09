import os.path
import sys

from .base_supplier import BaseSupplier
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

    def get_data_from_api_with_parameters(self, params: dict):
        """
        Получение данных от DKC API
        @param parameters:
        @return:
        """
        material_codes = params.get('material_codes')
        suppliers_parameters = params.get('suppliers_parameters')
        # print(f'{params=}')
        # print(f'{material_codes=} {suppliers_parameters=}')
        if material_codes and suppliers_parameters:
            dkc = None  # create dkc obj for all materials responses
            try:
                dkc = DkcObj()
            except DkcAccessTokenError as err:
                print(err)
            materials = get_materials(material_codes, params, dkc)
            # print('DKCSupplier materials:')
            # pprint.pprint(materials, indent=2)
            return materials
        return None

    def get_supplier_parameters_from_api(self) -> tuple:
        material_codes = ['4400003']
        materials = get_materials(material_codes)
        for material in materials:
            keys = tuple(material.__dict__.keys())
        # print(keys)
        return keys
