from .node import Node


class BaseHierarchicalTree:
    def __init__(self, root_node: Node = None, obj=None):
        self.root = root_node
        self.obj = obj

    def __str__(self):
        return f'{self.root}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def find_node_by_name(self, name: str):
        return self.root.find_node_by_name(name)

    def find_node_by_number(self, number: str):
        return self.root.find_node_by_number(number)

    def create_hierarchical_tree_parameters(self):
        """
        Создать иерархическое дерево
        @return:
        """

        def _create_hierarchical_tree():
            if self.root:
                return self.root.create_hierarchical_tree()
            return None

        return _create_hierarchical_tree()
