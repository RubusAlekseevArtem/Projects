import logging
import os.path
import sys

from .base_supplier import BaseSupplier
from .dkc_hierarchical_tree import DkcHierarchicalTreeParameters
from .hierarchical_tree import BaseHierarchicalTree
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

    def get_tree_view_parameters(self) -> BaseHierarchicalTree:
        dkc_hierarchical_tree_parameters = DkcHierarchicalTreeParameters(None)
        hierarchical_tree = dkc_hierarchical_tree_parameters.create_hierarchical_tree_parameters()
        return hierarchical_tree

    def get_data_from_api_with_parameters(self, params: dict):
        """
        Получение данных от DKC API
        @param parameters:
        @return:
        """
        material_codes = params.get('material_codes')
        if material_codes:
            dkc = None  # create dkc obj for all materials requests
            try:
                dkc = DkcObj()
            except DkcAccessTokenError as err:
                print(err)
                logging.error(err)
            return get_materials(material_codes, dkc)
        return None

    def get_supplier_parameters_from_api(self) -> tuple:
        material_codes = ['4400003']
        materials = get_materials(material_codes)
        for material in materials:
            keys = tuple(material.__dict__.keys())
        # print(keys)
        return keys
