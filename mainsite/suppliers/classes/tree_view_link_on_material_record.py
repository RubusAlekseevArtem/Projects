import os.path
import sys
from dataclasses import dataclass
from typing import List

sys.path.append(os.path.abspath(rf'..'))
from .id_counter import IdCounter
from DKC_API.data_classes.material_record import MaterialRecord


@dataclass
class MaterialInfoGroup:
    id: int | None = None,
    node_id: int | None = None,
    etim_class_id: str | None = None,
    name: str | None = None,
    type: str | None = None,
    series: str | None = None,
    country: str | None = None,
    unit: str | None = None,
    volume: float | None = None,
    weight: float | None = None,
    code: str | None = None,
    url: str | None = None,
    price: float | None = None,
    no_price: bool | None = None,
    barcode: List[str] | None = None,


@dataclass
class MaterialImageGroup:
    thumbnail_url: str | None = None,
    additional_images: List[str] | None = None,


@dataclass
class MaterialAttributesGroup:
    attributes: dict | None = None,


@dataclass
class MaterialEtimAttributesGroup:
    etim_attributes: dict | None = None,


@dataclass
class MaterialPackingGroup:
    packing: dict | None = None,


@dataclass
class MaterialAvgDeliveryGroup:
    avg_delivery: dict | None = None,


@dataclass
class MaterialAccessoriesGroup:
    accessories: List[str] | None = None,


@dataclass
class MaterialAccessoriesCodesGroup:
    accessories_codes: List[str] | None = None,


@dataclass
class MaterialSaleGroup:
    sale: List | None = None,

# class TreeViewLinkOnMaterialRecord:
#
#     def get_parameter_by_tree_id(self, index: int) -> dict | None:
#         """
#
#         @type index: material_index
#         """
#         if index >= len(self._material_records) or index < 0:
#             return
#         id_counter = IdCounter()
#         return {
#             id_counter.id: self._material_records[index],  # Материал DKC
#             id_counter.id: self._material_records[index].material,  # Материал
#             id_counter.id: MaterialInfoGroup(  # Информация по материалу
#                 self._material_records[index].material.id,
#                 self._material_records[index].material.node_id,
#                 self._material_records[index].material.etim_class_id,
#                 self._material_records[index].material.name,
#                 self._material_records[index].material.type,
#                 self._material_records[index].material.series,
#                 self._material_records[index].material.country,
#                 self._material_records[index].material.unit,
#                 self._material_records[index].material.volume,
#                 self._material_records[index].material.weight,
#                 self._material_records[index].material.code,
#                 self._material_records[index].material.url,
#                 self._material_records[index].material.price,
#                 self._material_records[index].material.no_price,
#                 self._material_records[index].material.barcode),
#             id_counter.id: MaterialImageGroup(  # Фото материала
#                 self._material_records[index].material.thumbnail_url,
#                 self._material_records[index].material.additional_images),
#             id_counter.id: MaterialAttributesGroup(  # Атрибуты материала
#                 self._material_records[index].material.attributes),
#             id_counter.id: MaterialEtimAttributesGroup(  # ETIM атрибуты материала
#                 self._material_records[index].material.etim_attributes),
#             id_counter.id: MaterialPackingGroup(
#                 self._material_records[index].material.packing),  # Фасовка
#             id_counter.id: MaterialAvgDeliveryGroup(
#                 self._material_records[index].material.avg_delivery),  # Средняя доставка
#             id_counter.id: MaterialAccessoriesGroup(
#                 self._material_records[index].material.accessories),  # Аксессуары
#             id_counter.id: MaterialAccessoriesCodesGroup(
#                 self._material_records[index].material.accessories_codes),  # Коды аксессуаров
#             id_counter.id: MaterialSaleGroup(
#                 self._material_records[index].material.sale),  # Скидка
#             id_counter.id: self._material_records[index].certificates,  # Сертификаты материала
#             id_counter.id: self._material_records[index].stock,  # Остатки на складах
#             id_counter.id: self._material_records[index].related,  # Сопутствующие материалы
#             id_counter.id: self._material_records[index].accessories,  # Аксессуары материала
#             id_counter.id: self._material_records[index].videos,  # Видео
#             id_counter.id: self._material_records[index].drawings_sketch,  # Эскизы чертежей
#             id_counter.id: self._material_records[index].description,  # Описание
#             id_counter.id: self._material_records[index].analogs,  # Аналоги
#             id_counter.id: self._material_records[index].specification,  # Пересчет спецификации
#         }
#
#     def __init__(self, material_records: List[MaterialRecord]):
#         self._material_records = material_records
