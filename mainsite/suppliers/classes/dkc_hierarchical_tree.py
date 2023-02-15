from .hierarchical_tree import BaseHierarchicalTree
from .node import Node


class DkcHierarchicalTree(BaseHierarchicalTree):
    def __init__(self):
        root_node = Node(
            'dkc_material', 'Материал DKC',
            [
                Node(
                    'general_material_parameter', 'Материал',
                    [
                        Node(
                            'info', 'Информация по материалу',
                            [

                            ],
                        ),
                        Node(
                            'photo', 'Фото материала',
                            [

                            ],
                        ),
                        Node(
                            'attributes', 'Атрибуты материала',
                            [

                            ],
                        ),
                        Node(
                            'etim_attributes', 'ETIM атрибуты материала',
                            [

                            ],
                        ),
                        Node(
                            'other', 'Другое',
                            [
                                Node(
                                    'packing', 'Фасовка',
                                    [

                                    ],
                                ),
                                Node(
                                    'avg_delivery', 'Средняя доставка',
                                    [

                                    ],
                                ),

                                Node(
                                    'accessories', 'Аксессуары',
                                    [

                                    ],
                                ),
                                Node(
                                    'accessories_codes', 'Коды аксессуаров',
                                    [

                                    ],
                                ),
                                Node(
                                    'sale', 'Скидка',
                                    [

                                    ],
                                ),
                            ],
                        ),
                    ]
                ),
                Node('certificates', 'Сертификаты материала'),
                Node('stock', 'Остатки на складах'),
                Node('related', 'Сопутствующие материалы'),
                Node('accessories', 'Аксессуары материала'),
                Node('videos', 'Видео'),
                Node('drawings_sketch', 'Эскизы чертежей'),
                Node('description', 'Описание'),
                Node('analogs', 'Аналоги'),
                Node('specification', 'Пересчет спецификации'),
            ]
        )
        super().__init__(root_node)
