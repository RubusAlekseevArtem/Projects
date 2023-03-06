import logging
from typing import List, Tuple

from .suppliers.base_supplier import BaseSupplier
from .suppliers.dkc_supplier import DKCSupplier


class SupplierProvider:
    MINIMUM_SUPPLIER_ID = 1

    def __init__(self):
        """
        Инициализация поставщиков
        """
        self._suppliers: Tuple[BaseSupplier] = (
            DKCSupplier(),
        )

    def _find_supplier(self, supplier_id: int):
        return list(filter(lambda supplier_: supplier_.pk == supplier_id, self._suppliers))

    def supplier_not_exists(self, supplier_id: int):
        return not self.supplier_exists(supplier_id)

    def supplier_exists(self, supplier_id: int):
        return supplier_id >= self.MINIMUM_SUPPLIER_ID

    def get_supplier_data(self, supplier_id: int, params: dict):
        """
        Попробуй выполнить скрипт через api поставщика
        @param supplier_id: id поставщика
        @param params: параметры
        @return: Данные или None
        """
        if self.supplier_not_exists(supplier_id):
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            return supplier[0].get_supplier_data(params)

    def get_supplier_tree_params(self, supplier_id: int):
        """
        Получить иерархическую структуру параметров поставщика
        @param supplier_id: id поставщика
        @return: параметры поставщика или None
        """
        if self.supplier_not_exists(supplier_id):
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            tree = supplier[0].get_supplier_tree()
            tree_params = tree.create_hierarchical_tree_parameters()
            return tree_params

    def get_filter_data_by_tree_numbers(self, supplier_id: int,
                                        supplier_data: List[dict],
                                        tree_numbers: List[str]) -> List | None:
        if self.supplier_not_exists(supplier_id):
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            result = []
            supplier_tree = supplier[0].get_supplier_tree()
            for material in supplier_data:
                result_obj = {}
                for tree_number in tree_numbers:
                    find_node = supplier_tree.find_node_by_number(tree_number)
                    try:
                        if find_node.have_function:
                            res = find_node.function(material)
                            result_obj[tree_number] = res
                    except AttributeError as err:
                        message = f'(name={tree_number}){find_node} не имеет функции ({err})'
                        print(message)
                        logging.error(message)
                result.append(result_obj)
            return result
