import logging
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
            self._suppliers: List[BaseSupplier] = suppliers
        else:
            self._suppliers: List[BaseSupplier] = [
                DKCSupplier(),
            ]

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

    def get_filter_data_by_tree_names(self, supplier_id: int,
                                      material_records: List[dict],
                                      tree_names: List[str]) -> List | None:
        if supplier_id < self.MINIMUM_SUPPLIER_ID:
            return
        supplier = self._find_supplier(supplier_id)
        if supplier:
            result = []
            supplier_parameter_tree = supplier[0].get_hierarchical_tree()
            for material in material_records:
                result_obj = {}
                for name in tree_names:
                    print(f'current name= {name}')
                    find_node = supplier_parameter_tree.root.find_child_node_by_number(name)
                    try:
                        # print(f'{find_node.have_function=}')
                        if find_node.have_function:
                            res = find_node.function(material)
                            print(f'result: {res}')
                            result_obj[name] = res
                    except AttributeError as err:
                        logging.error(f'(name={name}){find_node} не имеет функции ({err})')
                result.append(result_obj)
            return result
