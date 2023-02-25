from django.test import TestCase

from .func_node import FuncNode
from .node import Node


class NodeTests(TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_node(self):
        main_node = Node('root', 'Материал DKC').add_children([
            Node('general_params', 'Материал'),
            Node('material_certificates', 'Сертификаты материала'),
            Node('stock', 'Остатки на складах'),
        ])
        self.assertEqual(main_node.number, 'root')
        self.assertEqual(main_node.name, 'Материал DKC')
        self.assertEqual(main_node.has_children(), True)
        self.assertEqual(
            main_node, Node('root', 'Материал DKC').add_children(
                [
                    Node('general_params', 'Материал'),
                    Node('material_certificates', 'Сертификаты материала'),
                    Node('stock', 'Остатки на складах'),
                ]
            )
        )
        # print(main_node)

        self.assertEqual(main_node.find_child_node_by_name('123'), None)
        self.assertEqual(main_node.find_child_node_by_number('123'), None)
        self.assertNotEqual(main_node.find_child_node_by_name('Материал'), None)
        self.assertNotEqual(main_node.find_child_node_by_number('general_params'), None)


class FuncNodeTests(TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_func_node(self):
        def f_get_data():
            data = {'1': 1}
            return data

        def f_get_data_2():
            data = {'2': 2}
            return data

        def f_get_data_3():
            data = {'3': 3}
            return data

        func_node = FuncNode('id', 'test_func_name', f_get_data).add_children(
            [
                FuncNode('id_2', 'test_func_name_2', f_get_data_2),
                FuncNode('id_3', 'test_func_name_3', f_get_data_3),
            ]
        )

        self.assertEqual(func_node.number, 'id')
        self.assertEqual(func_node.name, 'test_func_name')
        self.assertEqual(func_node.fun, f_get_data)
        self.assertEqual(func_node.has_children(), True)
        self.assertEqual(
            func_node,
            FuncNode('id', 'test_func_name', f_get_data).add_children(
                [
                    FuncNode('id_2', 'test_func_name_2', f_get_data_2),
                    FuncNode('id_3', 'test_func_name_3', f_get_data_3),
                ]
            )
        )

        self.assertEqual(func_node.find_child_node_by_name('123'), None)
        self.assertEqual(func_node.find_child_node_by_number('123'), None)
        self.assertNotEqual(func_node.find_child_node_by_name('test_func_name_2'), None)
        self.assertNotEqual(func_node.find_child_node_by_number('id_3'), None)


# class FuncNodeCastToNodeTests(TestCase):
#     # def setUp(self) -> None:
#     #     pass
#     #
#     # def tearDown(self) -> None:
#     #     pass
#
#     def test_func_node_cast_to_node(self):
#         def f_get_data():
#             data = {'1': 1}
#             return data
#
#         def f_get_data_2():
#             data = {'2': 2}
#             return data
#
#         func_node = FuncNode('id', 'test_func_name', f_get_data).add_children(
#             [
#                 FuncNode('id_2', 'test_func_name_2', f_get_data_2),
#             ]
#         )
