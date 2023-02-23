from typing import Callable

from .node import Node


class FuncNode(Node):
    def __init__(self, number: str, name: str, fun: Callable[[], dict], parent=None):
        super().__init__(number, name, parent)
        # if not isinstance(fun(), dict):
        #     raise Exception('Function must be return dict')
        self.fun = fun

    def __str__(self):
        return f'{super().__str__()} f={self.fun.__name__}'

    def __repr__(self):
        return f'FuncNode({self.__str__()})'

    def __eq__(self, other):
        if isinstance(other, FuncNode):
            return super().__eq__(Node(self.number, self.name, self.parent)) and \
                self.fun == other.fun
        return False
