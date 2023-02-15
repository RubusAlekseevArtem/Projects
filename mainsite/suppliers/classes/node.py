from typing import List


class Node:
    def __init__(self, number: str, name: str, children=None):
        self.number = number
        self.name = name
        self.children: List[Node] = children

    def __str__(self):
        return f'{self.number} {self.name} {self.children}'

    def __repr__(self):
        return f'Node({self.__str__()})'

    def has_children(self):
        return self.children is not None
