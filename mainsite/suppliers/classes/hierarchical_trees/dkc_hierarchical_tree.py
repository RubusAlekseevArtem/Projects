from itertools import islice

from .base_hierarchical_tree import BaseHierarchicalTree
from ..nodes.func_node import FuncNode


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


def get_url_to_the_video(obj: dict):
    return list(map(lambda i: i.get('url'), get_video(obj)))


def get_cover(obj: dict):
    return list(map(lambda i: i.get('cover'), get_video(obj)))


def get_link_type(obj: dict):
    return list(map(lambda i: i.get('type'), get_video(obj)))


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
                                FuncNode('no_price', 'Никакой цены?',
                                         lambda o: get_info(o).get('no_price')),
                                FuncNode('barcode', 'Штрих-код',
                                         lambda o: get_info(o).get('barcode')),
                            ],
                        ),
                        FuncNode('photo', 'Фото материала', get_photo).add_children(
                            [
                                FuncNode(
                                    'thumbnail_url', 'Миниатюра материала',
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
                        FuncNode('accessories', 'Аксессуары',
                                 lambda o: get_general_material_parameter(o).get('accessories')),
                        FuncNode('accessories_codes', 'Коды аксессуаров',
                                 lambda o: get_general_material_parameter(o).get('accessories_codes')),
                        FuncNode('sale', 'Скидки на материал',
                                 lambda o: get_general_material_parameter(o).get('sale')),
                    ]
                ),
                FuncNode('certificates', 'Сертификаты',
                         lambda o: get_dkc_material(o).get('certificates')),
                FuncNode('stock', 'Остатки на складах',
                         lambda o: get_dkc_material(o).get('stock')),
                FuncNode('related', 'Сопутствующие материалы',
                         lambda o: get_dkc_material(o).get('related')),
                FuncNode('video', 'Видео', get_video).add_children(
                    [
                        FuncNode('url_to_the_video', 'Ссылка на видео',
                                 get_url_to_the_video),
                        FuncNode('cover', 'Ссылка на обложку видео', get_cover),
                        FuncNode('link_type', 'Тип ссылки видео', get_link_type),
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
