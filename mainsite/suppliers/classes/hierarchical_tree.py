from typing import List

from .node import Node


class BaseHierarchicalTree:
    def __init__(self, root_node: Node = None):
        self.root = root_node

    def __str__(self):
        return f'{self.root}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def _find_node_by_number(self, node: Node, number: str):
        def _find_node_by_number(nodes: List[Node], number: str):
            for node in nodes:
                if node.number == number:
                    return node
                elif node.has_children():
                    return _find_node_by_number(node.children, number)
            return None

        if node:
            if node.number == number:
                return node
            elif node.has_children():
                return _find_node_by_number(node.children, number)
        return None

    def find_node_by_number(self, number: str):
        return self._find_node_by_number(self.root, number)

    def _find_node_by_name(self, node: Node, name: str):
        def _find_node_by_name(nodes: List[Node], name: str):
            for node in nodes:
                if node.name == name:
                    return node
                elif node.has_children():
                    return _find_node_by_name(node.children, name)
            return None

        if node:
            if node.name == name:
                return node
            elif node.has_children():
                return _find_node_by_name(node.children, name)
        return None

    def find_node_by_name(self, name: str):
        return self._find_node_by_name(self.root, name)

    def _create_tree(self):
        if self.root:
            return self.root.create_node()
        return None

    def create_tree(self):
        return self._create_tree()
