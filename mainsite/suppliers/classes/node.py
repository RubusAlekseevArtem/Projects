from typing import List, Iterable


class NodeCreationError(Exception):
    """Node creation error"""

    def __init__(self):
        super().__init__(self.__doc__)


class Node:
    NUMBER_KEY = 'Number'
    NAME_KEY = 'Name'
    CHILDREN_KEY = 'Children'

    def __init__(self, number: str, name: str, parent=None):
        self.parent: Node = parent
        self.number = number
        self.name = name
        self.children: List[Node] = []
        # add unique number

    def __str__(self):
        return f'{self.number} {self.name} {self.children}'

    def __repr__(self):
        return f'Node({self.__str__()})'

    def has_parent(self) -> bool:
        return self.parent is not None

    def has_children(self) -> bool:
        return len(self.children) > 0

    def add_child(self, node):
        if not isinstance(node, Node):
            raise NodeCreationError()
        self.children.append(node)

    def add_children(self, nodes: Iterable):
        for node in nodes:
            self.add_child(node)

    def create_hierarchical_tree(self):
        def _create_node(node: Node):
            return {
                self.NUMBER_KEY: node.number,
                self.NAME_KEY: node.name,
                self.CHILDREN_KEY: [_create_node(child) for child in node.children]
            }

        return _create_node(self)

    def find_child_node_by_number(self, number: str):
        def _find_child_node_by_number(node: Node, number_: str):
            def __find_child_node_by_number(children: List[Node], number__: str):
                for child in children:
                    if child.number == number__:
                        return child
                    elif child.has_children():
                        return __find_child_node_by_number(child.children, number__)
                return None

            if node:
                if node.number == number_:
                    return node
                elif node.has_children():
                    return __find_child_node_by_number(node.children, number_)
            return None

        return _find_child_node_by_number(self, number)

    def find_child_node_by_name(self, name: str):
        def _find_child_node_by_name(node: Node, name_: str):
            def __find_child_node_by_name(children: List[Node], name__: str):
                for child in children:
                    if child.name == name__:
                        return child
                    elif child.has_children():
                        return __find_child_node_by_name(child.children, name__)
                return None

            if node:
                if node.name == name_:
                    return node
                elif node.has_children():
                    return __find_child_node_by_name(node.children, name_)
            return None

        return _find_child_node_by_name(self, name)
