from typing import Callable

from .node import Node


class FuncNode(Node):
    def __init__(self, number: str, name: str, function: Callable[[dict], dict] = None):
        super().__init__(number, name)
        self.function = function

    def __str__(self):
        return f'{super().__str__()} f={self.function.__name__ if self.function else self.function}'

    def __repr__(self):
        return f'FNode({self.__str__()})'

    def __eq__(self, other):
        if isinstance(other, FuncNode):
            return self.number == other.number and \
                self.name == other.name and \
                self.children == other.children and \
                self.function == other.function
        return False

    @property
    def have_function(self):
        return self.function is not None
