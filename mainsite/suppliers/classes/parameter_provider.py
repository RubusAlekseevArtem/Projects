import logging
from typing import List

from .base_supplier import BaseSupplier
from .dkc_supplier import DKCSupplier
from ..models import Supplier


class SupplierProvider:

    def __init__(self, suppliers: List[BaseSupplier] = None):
        if suppliers is not None:
            self.suppliers = suppliers
        else:
            self.suppliers = (
                DKCSupplier(),
            )

    def try_execute_api_by_name(self, supplier_name):
        """
        Попробуй выполнить запрос к поставщику через api по имени
        @param supplier_name:
        @return:
        """
        raise NotImplementedError()

    def try_update_parameters_by_id(self, supplier_id: int):
        """
        Попробуй выполнить запрос к поставщику через api по id
        @param supplier_id:
        @return:
        """
        if supplier_id < 1:
            return
        for supplier in self.suppliers:
            try:
                supplier_obj = Supplier.objects.all().filter(name=supplier.name)[0]
                print(f'{supplier_obj.id} == {supplier_id}')
                if supplier_obj.id == supplier_id:  # если есть такой поставщик
                    supplier.update_new_supplier_params()
                    return
            except IndexError as err:
                logging.error(err)
