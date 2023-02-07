from .base_supplier import BaseSupplier

import sys
import os.path

sys.path.append(os.path.abspath(rf'..'))

from DKC_API.main import get_materials


class DKCSupplier(BaseSupplier):
    def __init__(self, name: str = 'DKC API'):
        super().__init__(name)

    def get_supplier_parameters_from_api(self) -> tuple:
        material_codes = ['4400003']
        materials = get_materials(material_codes)
        for material in materials:
            keys = tuple(material.__dict__.keys())
        # print(keys)
        return keys
