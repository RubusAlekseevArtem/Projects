import logging
from abc import ABC, abstractmethod
from builtins import IndexError

from ..models import Supplier, SupplierParameter


class BaseSupplier(ABC):
    """
    BaseSupplier - абстарктный класс для создания поставщиков
    """

    @abstractmethod
    def __init__(self, name: str):
        """
        @param name: имя поставщика
        """
        self.name = name

    @abstractmethod
    def get_supplier_parameters_from_api(self) -> tuple:
        """
        Получить все параметры поставщика
        @return: кортеж строки
        """
        pass

    def update_new_supplier_params(self, supplier_params: tuple = None):
        """
        Обновить все новые паремеры поствщика из supplier_params
        @param supplier_params: параметры поставщика (по умолчанию = get_supplier_parameters_from_api())
        """
        try:
            if supplier_params is None:
                supplier_params = self.get_supplier_parameters_from_api()
            supplier = Supplier.objects.all().filter(name=self.name)[0]
            supplier_parameters_from_db = SupplierParameter.objects.all().filter(supplier__pk=supplier.pk)
            # print(f'{len(supplier_params)} > {len(supplier_parameters_from_db)}')
            if len(supplier_params) > len(supplier_parameters_from_db):  # если есть новые
                new_parameters = set(supplier_params) - set(supplier_parameters_from_db)  # разность множеств
                for new_parameter_name in new_parameters:
                    logging.info(f'Create new parameter \'{new_parameter_name}\' for \'{supplier.name}\'')
                    SupplierParameter.objects.create(supplier=supplier, parameter_name=new_parameter_name)
        except IndexError as err:
            logging.error(err)
