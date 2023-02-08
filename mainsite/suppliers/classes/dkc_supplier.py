import logging

from .base_supplier import BaseSupplier

import sys
import os.path

from ..models import Supplier

sys.path.append(os.path.abspath(rf'..'))

from DKC_API.main import get_materials


class DKCSupplier(BaseSupplier):
    def __init__(self, name: str = 'DKC API', pk=None):
        try:  # trying to get id from db
            supplier = Supplier.objects.all().filter(name=name)[0]
            pk = supplier.pk
        except IndexError as err:
            logging.error(err)
        super().__init__(name, pk)

    def get_supplier_parameters_from_api(self) -> tuple:
        material_codes = ['4400003']
        materials = get_materials(material_codes)
        for material in materials:
            keys = tuple(material.__dict__.keys())
        # print(keys)
        return keys

    def __str__(self):
        return f'DKCSupplier({super().__str__()})'
