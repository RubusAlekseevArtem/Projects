from abc import ABC, abstractmethod

from .hierarchical_tree import BaseHierarchicalTree


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
    def get_data_from_api_with_parameters(self, parameters: dict):
        """
        Получить данные из api с параметрами
        @param parameters: парметры
        """
        pass

    @abstractmethod
    def get_tree_view_parameters(self) -> BaseHierarchicalTree:
        """
        Получить иерархические параметры
        @rtype: параматры поставщика
        """
        pass
