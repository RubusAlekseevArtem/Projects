from .node import Node


class BaseHierarchicalTree:
    def __init__(self, root_node: Node = None):
        self.root = root_node

    def __str__(self):
        return f'{self.root}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def _create_hierarchical_tree(self):
        if self.root:
            return self.root.create_node()
        return None

    def find_node_by_name(self, name: str):
        return self.root.find_node_by_name(name)

    def find_node_by_number(self, number: str):
        return self.root.find_node_by_number(number)

    def create_hierarchical_tree(self):
        """
        Создать иерархическое дерево из данного класса
        @return:
        """
        return self._create_hierarchical_tree()
