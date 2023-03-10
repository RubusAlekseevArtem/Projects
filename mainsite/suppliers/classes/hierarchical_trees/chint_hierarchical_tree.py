from itertools import islice

from .base_hierarchical_tree import BaseHierarchicalTree
from ..nodes.func_node import FuncNode


def get_chint_product(obj: dict):
    return obj


def get_general_parameters(obj: dict):
    return dict(islice(get_chint_product(obj).items(), 0, 28))


def get_photo(obj: dict):
    return dict(islice(get_general_parameters(obj).items(), 15, 17))


def get_files(obj: dict):
    return get_chint_product(obj).get('files')


def get_url_to_document(obj: dict):
    return list(map(lambda i: i.get('file'), get_files(obj)))


def get_document_name(obj: dict):
    return list(map(lambda i: i.get('name'), get_files(obj)))


def get_document_date(obj: dict):
    return list(map(lambda i: i.get('date'), get_files(obj)))


class ChintHierarchicalTreeParameters(BaseHierarchicalTree):
    def __init__(self):
        root_node = FuncNode('chint_product', 'Продукт E-CHINT', get_chint_product).add_children(
            [
                FuncNode(
                    'general_parameters', 'Главные параметры',
                    get_general_parameters).add_children(
                    [
                        FuncNode('id', 'id',
                                 lambda o: get_general_parameters(o).get('id')),
                        FuncNode('parent_id', 'parent_id',
                                 lambda o: get_general_parameters(o).get('parent_id')),
                        FuncNode('full_name', 'full_name',
                                 lambda o: get_general_parameters(o).get('full_name')),
                        FuncNode('short_name', 'short_name',
                                 lambda o: get_general_parameters(o).get('short_name')),
                        FuncNode('name', 'name',
                                 lambda o: get_general_parameters(o).get('name')),
                        FuncNode('vendor_code', 'vendor_code',
                                 lambda o: get_general_parameters(o).get('vendor_code')),
                        FuncNode('b2b_illiquid', 'b2b_illiquid',
                                 lambda o: get_general_parameters(o).get('b2b_illiquid')),
                        FuncNode('b2b_new_аrticle', 'b2b_new_аrticle',
                                 lambda o: get_general_parameters(o).get('b2b_new_аrticle')),
                        FuncNode('out_of_price', 'out_of_price',
                                 lambda o: get_general_parameters(o).get('out_of_price')),
                        FuncNode('status_article', 'status_article',
                                 lambda o: get_general_parameters(o).get('status_article')),
                        FuncNode('pack_indivisibility', 'pack_indivisibility',
                                 lambda o: get_general_parameters(o).get('pack_indivisibility')),
                        FuncNode('unit_name', 'unit_name',
                                 lambda o: get_general_parameters(o).get('unit_name')),
                        FuncNode('unit_id', 'unit_id',
                                 lambda o: get_general_parameters(o).get('unit_id')),
                        FuncNode('brutto', 'brutto',
                                 lambda o: get_general_parameters(o).get('brutto')),
                        FuncNode('weight', 'weight',
                                 lambda o: get_general_parameters(o).get('weight')),
                        FuncNode('volume', 'volume',
                                 lambda o: get_general_parameters(o).get('volume')),
                        FuncNode('group_pack_name', 'group_pack_name',
                                 lambda o: get_general_parameters(o).get('group_pack_name')),
                        FuncNode('group_pack_id', 'group_pack_id',
                                 lambda o: get_general_parameters(o).get('group_pack_id')),
                        FuncNode('group_pack_brutto', 'group_pack_brutto',
                                 lambda o: get_general_parameters(o).get('group_pack_brutto')),
                        FuncNode('group_pack_weight', 'group_pack_weight',
                                 lambda o: get_general_parameters(o).get('group_pack_weight')),
                        FuncNode('group_pack_volume', 'group_pack_volume',
                                 lambda o: get_general_parameters(o).get('group_pack_volume')),
                        FuncNode('b2b', 'b2b',
                                 lambda o: get_general_parameters(o).get('b2b')),
                        FuncNode('cert', 'cert',
                                 lambda o: get_general_parameters(o).get('cert')),
                        FuncNode('price_group', 'price_group',
                                 lambda o: get_general_parameters(o).get('price_group')),
                        FuncNode('etim', 'etim',
                                 lambda o: get_general_parameters(o).get('etim')),
                        FuncNode('min', 'min',
                                 lambda o: get_general_parameters(o).get('min')),
                        FuncNode('pv', 'pv',
                                 lambda o: get_general_parameters(o).get('pv')),
                        FuncNode('avia', 'avia',
                                 lambda o: get_general_parameters(o).get('avia')),
                    ]
                ),
                FuncNode('properties', 'Свойства (тех характеристики)',
                         lambda o: get_chint_product(o).get('properties')),
                FuncNode('picture', 'Фото',
                         lambda o: get_chint_product(o).get('picture')),
                FuncNode('documents', 'Документы', get_files)
                # .add_children(
                #     [
                #         FuncNode('url_to_document', 'Ссылка на документ',
                #                  get_url_to_document),
                #         FuncNode('document_name', 'Наименование документа', get_document_name),
                #         FuncNode('document_date', 'Дата действительности документа', get_document_date),
                #     ]
                # ),
            ]
        )
        super().__init__(root_node)
