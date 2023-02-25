from typing import Callable

from .node import Node


def to_node(func_node):
    def create_node(_func_node) -> Node:
        node = Node(_func_node.number, _func_node.name)
        if _func_node.has_children():
            node.add_children(
                [to_node(child) for child in _func_node.children]
            )
        return node

    return create_node(func_node)


class FuncNode(Node):
    def __init__(self, number: str, name: str, fun: Callable[[], dict]):
        super().__init__(number, name)
        self.fun = fun

    def __str__(self):
        return f'{super().__str__()} f={self.fun.__name__}'

    def __repr__(self):
        return f'FuncNode({self.__str__()})'

    def __eq__(self, other):
        if isinstance(other, FuncNode):
            return self.number == other.number and \
                self.name == other.name and \
                self.children == other.children and \
                self.fun == other.fun
        return False


if __name__ == '__main__':
    a = FuncNode('id', 'test_func_name', lambda x: x).add_children(
        [
            FuncNode('id_2', 'test_func_name_2', lambda x: x),
            FuncNode('id_3', 'test_func_name_3', lambda x: x),
        ]
    )
    print(to_node(a))
