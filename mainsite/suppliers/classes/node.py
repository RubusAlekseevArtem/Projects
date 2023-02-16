import pprint
from typing import List


class Node:
    NUMBER_KEY = 'Number'
    NAME_KEY = 'Name'
    CHILDREN_KEY = 'Children'

    def __init__(self, number: str, name: str, children=None):
        if children is None:
            children = []
        self.number = number
        self.name = name
        self.children: List[Node] = children
        # add unique number

    def __str__(self):
        return f'{self.number} {self.name} {self.children}'

    def __repr__(self):
        return f'Node({self.__str__()})'

    def has_children(self):
        return len(self.children) > 0

    def create_node(self):
        def _create_node(node: Node):
            return {
                self.NUMBER_KEY: node.number,
                self.NAME_KEY: node.name,
                self.CHILDREN_KEY: [_create_node(child) for child in node.children]
            }

        return _create_node(self)

    def find_node_by_number(self, number: str):
        def _find_node_by_number(node: Node, number_: str):
            def __find_node_by_number(children: List[Node], number__: str):
                for child in children:
                    if child.number == number__:
                        return child
                    elif child.has_children():
                        return __find_node_by_number(child.children, number__)
                return None

            if node:
                if node.number == number_:
                    return node
                elif node.has_children():
                    return __find_node_by_number(node.children, number_)
            return None

        return _find_node_by_number(self, number)

    def find_node_by_name(self, name: str):
        def _find_node_by_name(node: Node, name_: str):
            def __find_node_by_name(children: List[Node], name__: str):
                for child in children:
                    if child.name == name__:
                        return child
                    elif child.has_children():
                        return __find_node_by_name(child.children, name__)
                return None

            if node:
                if node.name == name_:
                    return node
                elif node.has_children():
                    return __find_node_by_name(node.children, name_)
            return None

        return _find_node_by_name(self, name)


if __name__ == '__main__':
    main_node = Node(
        'root',
        'Материал DKC',
        [
            Node('general_params', 'Материал'),
            Node('material_certificates', 'Сертификаты материала'),
            Node('stock', 'Остатки на складах'),
        ]
    )
    pprint.pprint(main_node.create_node(), indent=4, sort_dicts=False)
