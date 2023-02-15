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
        return len(self.children)

    def create_node(self):
        def _create_node(node: Node):
            return {
                self.NUMBER_KEY: node.number,
                self.NAME_KEY: node.name,
                self.CHILDREN_KEY: [_create_node(child) for child in node.children]
            }

        return _create_node(self)


if __name__ == '__main__':
    node = Node(
        'root',
        'Материал DKC',
        [
            Node('general_params', 'Материал'),
            Node('material_certificates', 'Сертификаты материала'),
            Node('stock', 'Остатки на складах'),
        ]
    )
    pprint.pprint(node.create_node(), indent=4, sort_dicts=False)
