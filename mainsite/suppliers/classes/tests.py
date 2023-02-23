from django.test import TestCase

from .node import Node


class NodeTests(TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_node(self):
        main_node = Node('root', 'Материал DKC')
        main_node.add_children([
            Node('general_params', 'Материал'),
            Node('material_certificates', 'Сертификаты материала'),
            Node('stock', 'Остатки на складах'),
        ])
        self.assertEqual(main_node.number, 'root')
        self.assertEqual(main_node.name, 'Материал DKC')
        self.assertEqual(main_node.has_children(), True)
        self.assertEqual(main_node.has_parent(), False)
        # self.assertEqual(str(self.test_supplier), f'{self.name} ({str(self.is_outdated)[0]})')
