import logging
from abc import ABC, abstractmethod
from builtins import IndexError

from ..models import Supplier, SupplierParameter


class BaseSupplier(ABC):
    """
    BaseSupplier - абстарктный класс для создания поставщиков
    """

    @abstractmethod
    def __init__(self, name: str, pk: int = None):
        """
        @param pk: primary key поставщика
        @param name: имя поставщика
        """
        self.pk = pk
        self.name = name

    def __str__(self):
        return f'{self.pk}, {self.name}'

    def __repr__(self):
        return str(self)

    @abstractmethod
    def get_supplier_parameters_from_api(self) -> tuple:
        """
        Получить все параметры поставщика
        @return: кортеж строки
        """
        pass

    @abstractmethod
    def get_data_from_api_with_parameters(self, parameters: dict) -> object:
        """
        Получить данные из api с параметрами
        @param parameters: парметры
        """
        pass

    def update_new_supplier_params(self, supplier_parameters: tuple = None):
        """
        Обновить все новые паремеры поствщика из supplier_params
        @param supplier_parameters: параметры поставщика (по умолчанию = get_supplier_parameters_from_api())
        """
        try:
            if supplier_parameters is None:
                supplier_parameters = self.get_supplier_parameters_from_api()
            supplier = Supplier.objects.all().filter(name=self.name)[0]
            supplier_parameters_from_db = SupplierParameter.objects.all().filter(supplier__pk=supplier.pk)
            # print(f'{len(supplier_params)} > {len(supplier_parameters_from_db)}')
            if len(supplier_parameters) > len(supplier_parameters_from_db):  # если есть новые
                new_parameters = set(supplier_parameters) - set(supplier_parameters_from_db)  # разность множеств
                for new_parameter_name in new_parameters:
                    logging.info(f'Create new parameter \'{new_parameter_name}\' for \'{supplier.name}\'')
                    SupplierParameter.objects.create(supplier=supplier, parameter_name=new_parameter_name)
        except IndexError as err:
            logging.error(err)
