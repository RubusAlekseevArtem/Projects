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

    def get_data_with_parameters(self, supplier_id: int, params: dict):
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
            return supplier[0].get_data_from_api_with_parameters(params)

    def get_hierarchical_tree_parameters(self, supplier_id: int):
        """
        Получить иерархическую структуру параметров поставщика
        @param supplier_id: id поставщика
        @return: параметры поставщика или None
        """
        if self.supplier_not_exists(supplier_id):
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            return supplier[0].get_hierarchical_tree().create_hierarchical_tree_parameters()

    def get_filter_data_by_tree_names(self, supplier_id: int,
                                      material_records: List[dict],
                                      tree_names: List[str]) -> List | None:
        if self.supplier_not_exists(supplier_id):
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            result = []
            supplier_parameter_tree = supplier[0].get_hierarchical_tree()
            for material in material_records:
                result_obj = {}
                for name in tree_names:
                    find_node = supplier_parameter_tree.root.find_child_node_by_number(name)
                    try:
                        if find_node.have_function:
                            res = find_node.function(material)
                            result_obj[name] = res
                    except AttributeError as err:
                        message = f'(name={name}){find_node} не имеет функции ({err})'
                        print(message)
                        logging.error(message)
                result.append(result_obj)
            return result
