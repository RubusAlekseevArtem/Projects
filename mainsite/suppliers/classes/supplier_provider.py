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
            self._suppliers = suppliers
        else:
            self._suppliers = (
                DKCSupplier(),
            )

    def _find_supplier(self, supplier_id: int):
        return list(filter(lambda supplier_: supplier_.pk == supplier_id, self._suppliers))

    def get_data_with_parameters(self, supplier_id: int, params: dict):
        """
        Попробуй выполнить скрипт через api поставщика
        @param supplier_id: id поставщика
        @param params: параметры
        @return: Данные или None
        """
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            return supplier[0].get_data_from_api_with_parameters(params)

    def update_parameters_by_id(self, supplier_id: int):
        """
        Попробуй выполнить запрос к поставщику через api по id
        @param supplier_id: id поставщика
        @return: None
        """
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            supplier[0].update_new_supplier_params()

    def get_tree_view_supplier_parameters(self, supplier_id: int):
        """
        Получить параметры поставщиков в виде TreeView
        @param supplier_id: id поставщика
        @return: параметры поставщика или None
        """
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            return supplier[0].get_tree_view_parameters()
