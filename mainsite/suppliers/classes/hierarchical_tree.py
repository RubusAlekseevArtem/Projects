import inspect
import os.path
import pprint
import sys
from dataclasses import is_dataclass
from typing import List

sys.path.append(os.path.abspath(rf'..'))

from DKC_API.data_classes.material_record import MaterialRecord


class HierarchicalTreeException(Exception):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def __str__(self):
        return f'{self.cls} isn\'t dataclass'


class IdCounter:
    def __init__(self):
        self._id: int = 0

    @property
    def id(self):  # getter
        # print('get id')
        self._id += 1
        return self._id

    @id.setter
    def id(self, new_id: int):  # setter
        self._id = new_id


class Node:
    def __init__(self, id_: int, name: str, children=None):
        if children is None:
            children = []
        self.id_ = id_
        self.name = name
        self.children: List[Node] = children

    def add_children(self, children):
        print(children)

    def __str__(self):
        return f'{self.id_} {self.name} {self.children}'

    def __repr__(self):
        return self.__str__()


class HierarchicalTreeCreator:
    ID = 'Number'  # Number - id узла
    NAME = 'Name'  # Name - имя узла
    CHILDREN = 'Children'  # Children - дети

    def __init__(self, cls):
        if is_dataclass(cls):
            self._cls = cls
        else:
            raise HierarchicalTreeException(cls)

    def get_hierarchical_tree(self):
        def create_hierarchical_tree():
            def build_tree(id_counter, class_name, cls, indent=0):
                print(cls)
                current_node = Node(id_counter.id, class_name)
                # getmembers() returns all the members of an object
                # for members in inspect.getmembers(cls):
                #     # 1) To remove private and protected functions
                #     # 2) To remove other methods that doesn't start with an underscore
                #     if not members[0].startswith('_') and not inspect.ismethod(members[1]):
                #         if not inspect.ismethod(members[1]):
                child_classes = inspect.getclasstree([cls])
                print(child_classes)
                for child_class in child_classes:
                    if type(child_class[0]) != type(object):
                        current_children = build_tree(id_counter, child_class[0][0].__name__, child_class[0][0])
                        current_node.add_children(current_children)
                return current_node

            return build_tree(IdCounter(), self._cls.__name__, self._cls)

        return create_hierarchical_tree()


if __name__ == '__main__':
    hierarchical_tree = HierarchicalTreeCreator(MaterialRecord)
    material_record_tree = hierarchical_tree.get_hierarchical_tree()
    pprint.pprint(material_record_tree, indent=3)
