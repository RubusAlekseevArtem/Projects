from abc import ABC, abstractmethod

from .hierarchical_tree import BaseHierarchicalTree


class BaseSupplier(ABC):
    """
    BaseSupplier - абстарктный класс поставщика
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
        return self.__str__()

    @abstractmethod
    def get_data_from_api_with_parameters(self, params: dict):
        """
        Получить данные из api с параметрами
        @param params:
        """
        pass

    @abstractmethod
    def get_hierarchical_tree(self) -> BaseHierarchicalTree:
        """
        Получить иерархическое дерево прараметров поставщика
        @return:
        """
        pass
