import pprint

from django.test import TestCase

from .dkc_hierarchical_tree import DkcHierarchicalTreeParameters
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
        self.assertEqual(func_node.function, f_get_data)
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

        test_node = FuncNode('dkc_material', 'Материал DKC', lambda o: o).add_children(
            [
                FuncNode(
                    'general_material_parameter',
                    'Общие параметры материала',
                    lambda o: o).add_children(
                    [
                        FuncNode('info', 'Информация по материалу', lambda o: o).add_children(
                            [
                                FuncNode('id', 'id', lambda o: o),
                                FuncNode('node_id', 'node_id', lambda o: o),
                                FuncNode('etim_class_id', 'etim_class_id', lambda o: o),
                                FuncNode('name', 'Название', lambda o: o),
                                FuncNode('type', 'Тип', lambda o: o),
                                FuncNode('series', 'Серия', lambda o: o),
                                FuncNode('country', 'Страна', lambda o: o),
                                FuncNode('unit', 'Единица измерения', lambda o: o),
                                FuncNode('volume', 'Объем', lambda o: o),
                                FuncNode('weight', 'Вес', lambda o: o),
                                FuncNode('code', 'Код материала', lambda o: o),
                                FuncNode('url', 'Ссылка на материал', lambda o: o),
                                FuncNode('price', 'Цена', lambda o: o),
                                FuncNode('no_price', 'Цены нет', lambda o: o),
                                FuncNode('barcode', 'Штрих-код', lambda o: o),
                            ],
                        ),
                        FuncNode('photo', 'Фото материала', lambda o: o).add_children(
                            [
                                FuncNode(
                                    'thumbnail_url', 'Миниатюра', lambda o: o),
                                FuncNode(
                                    'additional_images',
                                    'Дополнительные изображения', lambda o: o),
                            ],
                        ),
                        FuncNode('attributes', 'Атрибуты материала', lambda o: o),
                        FuncNode('etim_attributes', 'ETIM атрибуты материала', lambda o: o),
                        FuncNode('packing', 'Фасовка', lambda o: o),
                        FuncNode('avg_delivery', 'Средняя доставка', lambda o: o),
                        FuncNode('accessories', 'Аксессуары материала', lambda o: o),
                        FuncNode('accessories_codes', 'Коды аксессуаров', lambda o: o),
                        FuncNode('sale', 'Скидки на материал', lambda o: o),
                    ]
                ),
                FuncNode('certificates', 'Сертификаты материала', lambda o: o),
                FuncNode('stock', 'Остатки на складах', lambda o: o),
                FuncNode('related', 'Сопутствующие материалы', lambda o: o),
                FuncNode('video', 'Видео', lambda o: o).add_children(
                    [
                        FuncNode('url_to_the_video', 'Ссылка', lambda o: o),
                        FuncNode('cover', 'Обложка', lambda o: o),
                        FuncNode('link_type', 'Тип ссылки', lambda o: o),
                    ]
                ),
                FuncNode('drawings_sketch', 'Эскизы чертежей', lambda o: o),
                FuncNode('description', 'Описание', lambda o: o),
                FuncNode('analogs', 'Аналоги', lambda o: o),
                FuncNode('specification', 'Пересчет спецификации', lambda o: o),
            ]
        )

        self.assertNotEqual(test_node.find_child_node_by_number('dkc_material'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('general_material_parameter'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('info'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('id'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('node_id'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('etim_class_id'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('name'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('type'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('series'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('country'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('unit'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('volume'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('weight'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('code'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('url'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('price'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('no_price'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('barcode'), None)

        self.assertNotEqual(test_node.find_child_node_by_number('photo'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('attributes'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('etim_attributes'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('packing'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('sale'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('certificates'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('video'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('url_to_the_video'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('cover'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('link_type'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('drawings_sketch'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('description'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('analogs'), None)
        self.assertNotEqual(test_node.find_child_node_by_number('specification'), None)


class DkcHierarchicalTreeParametersTests(TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_func(self):
        d = DkcHierarchicalTreeParameters()
        # self.assertNotEqual(d.find_child_node_by_number('dkc_material'), None)
        # self.assertNotEqual(d.find_child_node_by_number('general_material_parameter'), None)
        # self.assertNotEqual(d.find_child_node_by_number('info'), None)
        # self.assertNotEqual(d.find_child_node_by_number('id'), None)
        # self.assertNotEqual(d.find_child_node_by_number('node_id'), None)
        # self.assertNotEqual(d.find_child_node_by_number('etim_class_id'), None)
        # self.assertNotEqual(d.find_child_node_by_number('name'), None)
        # self.assertNotEqual(d.find_child_node_by_number('type'), None)
        # self.assertNotEqual(d.find_child_node_by_number('series'), None)
        # self.assertNotEqual(d.find_child_node_by_number('country'), None)
        # self.assertNotEqual(d.find_child_node_by_number('unit'), None)
        # self.assertNotEqual(d.find_child_node_by_number('volume'), None)
        # self.assertNotEqual(d.find_child_node_by_number('weight'), None)
        # self.assertNotEqual(d.find_child_node_by_number('code'), None)
        # self.assertNotEqual(d.find_child_node_by_number('url'), None)
        # self.assertNotEqual(d.find_child_node_by_number('price'), None)
        # self.assertNotEqual(d.find_child_node_by_number('no_price'), None)
        # self.assertNotEqual(d.find_child_node_by_number('barcode'), None)
        # self.assertNotEqual(d.find_child_node_by_number('photo'), None)
        # self.assertNotEqual(d.find_child_node_by_number('attributes'), None)
        # self.assertNotEqual(d.find_child_node_by_number('etim_attributes'), None)
        # self.assertNotEqual(d.find_child_node_by_number('packing'), None)
        # self.assertNotEqual(d.find_child_node_by_number('sale'), None)
        # self.assertNotEqual(d.find_child_node_by_number('certificates'), None)
        # self.assertNotEqual(d.find_child_node_by_number('video'), None)
        # self.assertNotEqual(d.find_child_node_by_number('url_to_the_video'), None)
        # self.assertNotEqual(d.find_child_node_by_number('cover'), None)
        # self.assertNotEqual(d.find_child_node_by_number('link_type'), None)
        # self.assertNotEqual(d.find_child_node_by_number('drawings_sketch'), None)
        # self.assertNotEqual(d.find_child_node_by_number('description'), None)
        # self.assertNotEqual(d.find_child_node_by_number('analogs'), None)
        # self.assertNotEqual(d.find_child_node_by_number('specification'), None)
