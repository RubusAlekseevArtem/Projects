from .hierarchical_tree import BaseHierarchicalTree


class DkcHierarchicalTree(BaseHierarchicalTree):
    def __init__(self):
        super().__init__()
        print(self.find_node_by_name('123'))
