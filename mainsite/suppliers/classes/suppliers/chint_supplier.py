import os.path
import sys

from ..hierarchical_trees.chint_hierarchical_tree import ChintHierarchicalTreeParameters
from ..suppliers.base_supplier import BaseSupplier
from ...models import Supplier

p = os.path.abspath(rf'.')
# print(p)
sys.path.append(p)
from CHINT_API.main import get_products


class ChintSupplier(BaseSupplier):

    def __init__(self, name: str = 'E-CHINT API', pk=None):
        # trying to get id from db
        supplier = Supplier.objects.all().filter(name=name)
        print(supplier)
        if supplier:
            pk = supplier[0].pk
        super().__init__(name, pk)

    def __str__(self):
        return f'ChintSupplier({super().__str__()})'

    def get_supplier_tree(self):
        return ChintHierarchicalTreeParameters()

    def get_supplier_data(self, params: dict):
        """
        Получение данных из E-CHINT API
        @param params:
        @return:
        """
        material_codes = params.get('material_codes')
        if material_codes:
            return get_products(material_codes)
        return []
