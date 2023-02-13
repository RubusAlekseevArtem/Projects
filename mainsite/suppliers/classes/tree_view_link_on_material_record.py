import os.path
import sys
from dataclasses import dataclass
from typing import List

from .hierarchical_tree import IdCounter

sys.path.append(os.path.abspath(rf'..'))
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


class TreeViewLinkOnMaterialRecord:
    def __init__(self, material_record: MaterialRecord):
        id_counter = IdCounter()
        self.material_record = material_record
        self.links = {
            id_counter.id: self.material_record,  # Материал DKC
            id_counter.id: self.material_record.material,  # Материал
            id_counter.id: MaterialInfoGroup(  # Информация по материалу
                self.material_record.material.id,
                self.material_record.material.node_id,
                self.material_record.material.etim_class_id,
                self.material_record.material.name,
                self.material_record.material.type,
                self.material_record.material.series,
                self.material_record.material.country,
                self.material_record.material.unit,
                self.material_record.material.volume,
                self.material_record.material.weight,
                self.material_record.material.code,
                self.material_record.material.url,
                self.material_record.material.price,
                self.material_record.material.no_price,
                self.material_record.material.barcode),
            id_counter.id: MaterialImageGroup(  # Фото материала
                self.material_record.material.thumbnail_url,
                self.material_record.material.additional_images),
            id_counter.id: MaterialAttributesGroup(  # Атрибуты материала
                self.material_record.material.attributes),
            id_counter.id: MaterialEtimAttributesGroup(  # ETIM атрибуты материала
                self.material_record.material.etim_attributes),
            id_counter.id: MaterialPackingGroup(
                self.material_record.material.packing),  # Фасовка
            id_counter.id: MaterialAvgDeliveryGroup(
                self.material_record.material.avg_delivery),  # Средняя доставка
            id_counter.id: MaterialAccessoriesGroup(
                self.material_record.material.accessories),  # Аксессуары
            id_counter.id: MaterialAccessoriesCodesGroup(
                self.material_record.material.accessories_codes),  # Коды аксессуаров
            id_counter.id: MaterialSaleGroup(
                self.material_record.material.sale),  # Скидка
            id_counter.id: self.material_record.certificates,  # Сертификаты материала
            id_counter.id: self.material_record.stock,  # Остатки на складах
            id_counter.id: self.material_record.related,  # Сопутствующие материалы
            id_counter.id: self.material_record.accessories,  # Аксессуары материала
            id_counter.id: self.material_record.videos,  # Видео
            id_counter.id: self.material_record.drawings_sketch,  # Эскизы чертежей
            id_counter.id: self.material_record.description,  # Описание
            id_counter.id: self.material_record.analogs,  # Аналоги
            id_counter.id: self.material_record.specification,  # Пересчет спецификации
        }
