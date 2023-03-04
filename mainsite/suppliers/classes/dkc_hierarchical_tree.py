from itertools import islice

from .func_node import FuncNode
from .hierarchical_tree import BaseHierarchicalTree


def get_dkc_material(obj: dict):
    return obj


def get_general_material_parameter(obj: dict):
    return get_dkc_material(obj).get('material')


def get_info(obj: dict):
    general_material_parameter = get_general_material_parameter(obj)
    if general_material_parameter is None:
        return None
    else:
        return dict(islice(general_material_parameter.items(), 0, 15))  # slice first 15 keys and values


def get_photo(obj: dict):
    return dict(islice(get_general_material_parameter(obj).items(), 15, 17))


def get_video(obj: dict):
    return get_dkc_material(obj).get('video')


class DkcHierarchicalTreeParameters(BaseHierarchicalTree):
    def __init__(self):
        root_node = FuncNode('dkc_material', 'Материал DKC', get_dkc_material).add_children(
            [
                FuncNode(
                    'general_material_parameter',
                    'Общие параметры материала',
                    get_general_material_parameter).add_children(
                    [
                        FuncNode('info', 'Информация по материалу', get_info).add_children(
                            [
                                FuncNode('id', 'id',
                                         lambda o: get_info(o).get('id')),
                                FuncNode('node_id', 'node_id',
                                         lambda o: get_info(o).get('node_id')),
                                FuncNode('etim_class_id', 'etim_class_id',
                                         lambda o: get_info(o).get('etim_class_id')),
                                FuncNode('name', 'Название',
                                         lambda o: get_info(o).get('name')),
                                FuncNode('type', 'Тип',
                                         lambda o: get_info(o).get('type')),
                                FuncNode('series', 'Серия',
                                         lambda o: get_info(o).get('series')),
                                FuncNode('country', 'Страна',
                                         lambda o: get_info(o).get('country')),
                                FuncNode('unit', 'Единица измерения',
                                         lambda o: get_info(o).get('unit')),
                                FuncNode('volume', 'Объем',
                                         lambda o: get_info(o).get('volume')),
                                FuncNode('weight', 'Вес',
                                         lambda o: get_info(o).get('weight')),
                                FuncNode('code', 'Код материала',
                                         lambda o: get_info(o).get('code')),
                                FuncNode('url', 'Ссылка на материал',
                                         lambda o: get_info(o).get('url')),
                                FuncNode('price', 'Цена',
                                         lambda o: get_info(o).get('price')),
                                FuncNode('no_price', 'Цены нет',
                                         lambda o: get_info(o).get('no_price')),
                                FuncNode('barcode', 'Штрих-код',
                                         lambda o: get_info(o).get('barcode')),
                            ],
                        ),
                        FuncNode('photo', 'Фото материала', get_photo).add_children(
                            [
                                FuncNode(
                                    'thumbnail_url', 'Миниатюра',
                                    lambda o: get_photo(o).get('thumbnail_url')),
                                FuncNode(
                                    'additional_images',
                                    'Дополнительные изображения',
                                    lambda o: get_photo(o).get('additional_images')),
                            ],
                        ),
                        FuncNode('attributes', 'Атрибуты материала',
                                 lambda o: get_general_material_parameter(o).get('attributes')),
                        FuncNode('etim_attributes', 'ETIM атрибуты материала',
                                 lambda o: get_general_material_parameter(o).get('etim_attributes')),
                        FuncNode('packing', 'Фасовка',
                                 lambda o: get_general_material_parameter(o).get('packing')),
                        FuncNode('avg_delivery', 'Средняя доставка',
                                 lambda o: get_general_material_parameter(o).get('avg_delivery')),
                        FuncNode('accessories', 'Аксессуары материала',
                                 lambda o: get_general_material_parameter(o).get('accessories')),
                        FuncNode('accessories_codes', 'Коды аксессуаров',
                                 lambda o: get_general_material_parameter(o).get('accessories_codes')),
                        FuncNode('sale', 'Скидки на материал',
                                 lambda o: get_general_material_parameter(o).get('sale')),
                    ]
                ),
                FuncNode('certificates', 'Сертификаты материала',
                         lambda o: get_dkc_material(o).get('certificates')),
                FuncNode('stock', 'Остатки на складах',
                         lambda o: get_dkc_material(o).get('stock')),
                FuncNode('related', 'Сопутствующие материалы',
                         lambda o: get_dkc_material(o).get('related')),
                FuncNode('video', 'Видео', get_video).add_children(
                    [
                        FuncNode('url_to_the_video', 'Ссылка',
                                 lambda o: get_video(o).get('url')),
                        FuncNode('cover', 'Обложка',
                                 lambda o: get_video(o).get('cover')),
                        FuncNode('link_type', 'Тип ссылки',
                                 lambda o: get_video(o).get('type')),
                    ]
                ),
                FuncNode('drawings_sketch', 'Эскизы чертежей',
                         lambda o: get_dkc_material(o).get('drawings_sketch')),
                FuncNode('description', 'Описание',
                         lambda o: get_dkc_material(o).get('description')),
                FuncNode('analogs', 'Аналоги',
                         lambda o: get_dkc_material(o).get('analogs')),
                FuncNode('specification', 'Пересчет спецификации',
                         lambda o: get_dkc_material(o).get('specification')),
            ]
        )
        super().__init__(root_node)

# class AbstractMaterialParser(ABC):
#
#     def parse_object(self, json_obj) -> Node:
#         parent = Node('', '')
#         parent0 = parent
#         for node in json_obj:
#             new_node = self._parse_object0(node, parent, parent0)
#             if new_node != parent0:
#                 parent.add_child(new_node)
#                 parent = new_node
#         return parent
#
#     @abstractmethod
#     def _parse_object0(self, json_obj: dict, parent: Node, node: Node):
#         pass
#
#
# class MaterialParser(AbstractMaterialParser):
#     def _parse_object0(self, json_obj: dict, parent: Node, node: Node):
#         match json_obj:
#             case 'material':
#                 return json_obj.get('material')
#             case _:
#                 print(json_obj)
#         return node
#
#
# if __name__ == '__main__':
#     mp = MaterialParser()
#     with open(r"C:\Users\alekseev_a_practik\Downloads\data (6).txt", encoding='utf-8') as file:
#         json_objects = json.load(file)
#         # pprint.pprint(json_obj)
#         parsed_object = mp.parse_object(json_objects)
#         pprint.pprint(parsed_object)
