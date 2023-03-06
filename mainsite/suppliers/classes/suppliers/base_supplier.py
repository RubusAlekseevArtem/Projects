from abc import ABC, abstractmethod

from ..hierarchical_trees.base_hierarchical_tree import BaseHierarchicalTree


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
    def get_supplier_data(self, params: dict):
        """
        Получить данные поставщика с параметрами
        @param params:
        """
        pass

    @abstractmethod
    def get_supplier_tree(self) -> BaseHierarchicalTree:
        """
        Получить иерархическое дерево поставщика
        @return:
        """
        pass
