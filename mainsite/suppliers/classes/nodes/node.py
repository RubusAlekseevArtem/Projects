from typing import List, Iterable


class NodeCreationError(Exception):
    """Node creation error"""

    def __init__(self):
        super().__init__(self.__doc__)


class UniqueNodeCreationError(Exception):
    """Error creating a unique node number"""

    def __init__(self, repeated, list_numbers):
        """

        @param repeated:repeated element
        @param list_numbers: list numbers
        """
        super().__init__(f'Error creating a unique node number\n{repeated} in {list_numbers}')


class Node:
    NUMBER_KEY = 'Number'
    NAME_KEY = 'Name'
    CHILDREN_KEY = 'Children'

    def __init__(self, number: str, name: str):
        self.number = number
        self.name = name
        self.children: List[Node] = []

    def __str__(self):
        return f'{self.number} {self.name} {self.children}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.number == other.number and \
                self.name == other.name and \
                self.children == other.children
        return False

    def has_children(self) -> bool:
        return len(self.children) > 0

    def add_child(self, node):
        if not isinstance(node, Node):
            raise NodeCreationError()
        self.children.append(node)
        return self

    def add_children(self, nodes: Iterable, check_unique_numbers=True):
        for node in nodes:
            self.add_child(node)
        if check_unique_numbers:
            self.check_parents_numbers()
        return self

    def check_parents_numbers(self, unique_number=True):
        def _get_parents_numbers(children, result_list=None):
            if result_list is None:
                result_list = []
            for node in children:
                if node.has_children():
                    _get_parents_numbers(node.children, result_list)
                if node.number in result_list and unique_number:
                    raise UniqueNodeCreationError(node.number, result_list)  # tree should not have duplicate numbers
                result_list.append(node.number)

        if self.has_children():
            _get_parents_numbers(self.children, [self.number])

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
            if node:
                if node.number == number_:
                    return node
                elif node.has_children():
                    for child in node.children:
                        find_node = _find_child_node_by_number(child, number_)
                        if find_node:
                            return find_node
            return None

        return _find_child_node_by_number(self, number)

    def find_child_node_by_name(self, name: str):
        def _find_child_node_by_name(node: Node, name_: str):
            if node:
                if node.name == name_:
                    return node
                elif node.has_children():
                    for child in node.children:
                        find_node = _find_child_node_by_name(child, name_)
                        if find_node:
                            return find_node
            return None

        return _find_child_node_by_name(self, name)
