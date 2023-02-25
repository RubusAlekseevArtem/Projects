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
        return f'Node({self.__str__()})'

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.number == other.number and \
                self.name == other.name and \
                self.children == other.children
        return False

    def has_children(self) -> bool:
        return len(self.children) > 0

    def _add_child(self, node):
        if not isinstance(node, Node):
            raise NodeCreationError()
        self.children.append(node)
        return self

    def add_children(self, nodes: Iterable, check_unique_numbers=True):
        for node in nodes:
            self._add_child(node)
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
        return self

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


if __name__ == '__main__':
    main_node = Node('root', 'Материал DKC').add_children([
        Node('general_params', 'Материал').add_children([
            Node('general_params', 'Сертификат__')
        ]),
        Node('material_certificates', 'Сертификаты материала'),
        Node('stock', 'Остатки на складах'),
    ])
    print(main_node)
