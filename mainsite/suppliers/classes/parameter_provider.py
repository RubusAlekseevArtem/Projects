from typing import List

from .base_supplier import BaseSupplier
from .dkc_supplier import DKCSupplier


class SupplierProvider:
    MINIMUM_SUPPLIER_ID = 1

    def __init__(self, suppliers: List[BaseSupplier] = None):
        """
        Инициализация доступных поставщиков
        @param suppliers:
        """
        if suppliers is not None:
            self.suppliers = suppliers
        else:
            self.suppliers = (
                DKCSupplier(),
            )

    def try_execute_script_with_parameters(self, supplier_id: int, parameters=None):
        """
        Попробуй выполнить скрипт через api поставщика
        @param parameters: словарь параметров
        @param supplier_id: id поставщика
        @return: None
        """
        if parameters is None:
            parameters = {}
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = list(filter(lambda supplier_: supplier_.pk == supplier_id, self.suppliers))
        if supplier:
            supplier[0].get_data_from_api_with_parameters(parameters)

    def try_update_parameters_by_id(self, supplier_id: int):
        """
        Попробуй выполнить запрос к поставщику через api по id
        @param supplier_id: id поставщика
        @return: None
        """
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = list(filter(lambda supplier_: supplier_.pk == supplier_id, self.suppliers))
        if supplier:
            supplier[0].update_new_supplier_params()
