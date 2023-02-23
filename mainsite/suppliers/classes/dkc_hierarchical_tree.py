from .hierarchical_tree import BaseHierarchicalTree
from .node import Node
from .func_node import FuncNode


class DkcHierarchicalTreeParameters(BaseHierarchicalTree):
    def dkc_material(self):
        return self.obj

    def general_material_parameter(self):
        return self.dkc_material().get('general_material_parameter')

    def __init__(self, obj: dict):
        root_node = Node('dkc_material', 'Материал DKC').add_children(
            [
                Node('general_material_parameter', 'Общие параметры материала').add_children(
                    [
                        Node('info', 'Информация по материалу').add_children(
                            [
                                Node(
                                    'id', 'id',
                                ),
                                Node(
                                    'node_id', 'node_id',
                                ),
                                Node(
                                    'etim_class_id', 'etim_class_id',
                                ),
                                Node(
                                    'name', 'Название',
                                ),
                                Node(
                                    'type', 'Тип',
                                ),
                                Node(
                                    'series', 'Серия',
                                ),
                                Node(
                                    'country', 'Страна',
                                ),
                                Node(
                                    'unit', 'Единица измерения',
                                ),
                                Node(
                                    'volume', 'Объем',
                                ),
                                Node(
                                    'weight', 'Вес',
                                ),
                                Node(
                                    'code', 'Код материала',
                                ),
                                Node(
                                    'url', 'Ссылка на материал',
                                ),
                                Node(
                                    'price', 'Цена',
                                ),
                                Node(
                                    'no_price', 'Цены нет',
                                ),
                                Node(
                                    'barcode', 'Штрих-код',
                                ),
                            ],
                        ),
                        Node('photo', 'Фото материала').add_children(
                            [
                                Node(
                                    'thumbnail_url', 'Миниатюра',
                                ),
                                Node(
                                    'additional_images', 'Дополнительные изображения',
                                ),
                            ],
                        ),
                        Node(
                            'attributes', 'Атрибуты материала',
                        ),
                        Node(
                            'etim_attributes', 'ETIM атрибуты материала',
                        ),
                        Node(
                            'packing', 'Фасовка',
                        ),
                        Node(
                            'avg_delivery', 'Средняя доставка',
                        ),
                        Node(
                            'accessories', 'Аксессуары',
                        ),
                        Node(
                            'accessories_codes', 'Коды аксессуаров',
                        ),
                        Node(
                            'sale', 'Скидки на материал',
                        ),
                    ]
                ),
                Node('certificates', 'Сертификаты материала', ),
                Node('stock', 'Остатки на складах'),
                Node('related', 'Сопутствующие материалы'),
                Node('accessories', 'Аксессуары материала'),
                Node('videos', 'Видео').add_children(
                    [
                        Node('url', 'Ссылка'),
                        Node('cover', 'Обложка'),
                        Node('type', 'Тип ссылки'),
                    ]
                ),
                Node('drawings_sketch', 'Эскизы чертежей'),
                Node('description', 'Описание'),
                Node('analogs', 'Аналоги'),
                Node('specification', 'Пересчет спецификации'),
            ]
        )
        super().__init__(root_node, obj)
