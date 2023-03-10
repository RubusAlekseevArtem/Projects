import os.path
import sys

from ..hierarchical_trees.dkc_hierarchical_tree import DkcHierarchicalTreeParameters
from ..suppliers.base_supplier import BaseSupplier
from ...models import Supplier

p = os.path.abspath(rf'.')
# print(p)
sys.path.append(p)
from DKC_API.dkc_catalog_material import get_dkc_materials


class DKCSupplier(BaseSupplier):

    def __init__(self, name: str = 'DKC API', pk=None):
        # trying to get id from db
        supplier = Supplier.objects.all().filter(name=name)
        if supplier:
            pk = supplier[0].pk
        super().__init__(name, pk)

    def __str__(self):
        return f'DKCSupplier({super().__str__()})'

    def get_supplier_tree(self):
        return DkcHierarchicalTreeParameters()

    def get_supplier_data(self, params: dict):
        """
        Получение данных от DKC API
        @param params:
        @return:
        """
        material_codes = params.get('material_codes')
        if material_codes:
            return get_dkc_materials(material_codes)
        return []
