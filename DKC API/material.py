from dataclasses import dataclass
from json import JSONEncoder, dumps
from typing import List

from private_file import INDENT


@dataclass
class Material(JSONEncoder):
    id: int = None,
    node_id: int = None,
    etim_class_id: str = None,
    name: str = None,
    type: str = None,
    series: str = None,
    country: str = None,
    unit: str = None,
    volume: float = None,
    weight: float = None,
    code: str = None,
    url: str = None,
    price: float = None,
    no_price: bool = None,
    barcode: List[str] = None,
    thumbnail_url: str = None,
    additional_images: List[str] = None,
    attributes: dict = None,
    etim_attributes: dict = None,
    packing: dict = None,
    avg_delivery: dict = None,
    accessories: List[str] = None,
    accessories_codes: List[str] = None,
    sale: List = None

    def obj_dict(self):
        return self.__dict__

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=INDENT)

    # def __init__(
    #         self,
    #         id: int = None,
    #         node_id: int = None,
    #         etim_class_id: str = None,
    #         name: str = None,
    #         type: str = None,
    #         series: str = None,
    #         country: str = None,
    #         unit: str = None,
    #         volume: float = None,
    #         weight: float = None,
    #         code: str = None,
    #         url: str = None,
    #         price: float = None,
    #         no_price: bool = None,
    #         barcode: List[str] = None,
    #         thumbnail_url: str = None,
    #         additional_images: List[str] = None,
    #         attributes: dict = None,
    #         etim_attributes: dict = None,
    #         packing: dict = None,
    #         avg_delivery: dict = None,
    #         accessories: List[str] = None,
    #         accessories_codes: List[str] = None,
    #         sale: List = None,
    # ):
    #     self.weight = weight
    #     self.code = code
    #     self.url = url
    #     self.price = price
    #     self.no_price = no_price
    #     self.barcode = barcode
    #     self.thumbnail_url = thumbnail_url
    #     self.additional_images = additional_images
    #     self.attributes = attributes
    #     self.etim_attributes = etim_attributes
    #     self.packing = packing
    #     self.avg_delivery = avg_delivery
    #     self.accessories = accessories
    #     self.sale = sale
    #     self.accessories_codes = accessories_codes
    #     self.volume = volume
    #     self.unit = unit
    #     self.country = country
    #     self.series = series
    #     self.type = type
    #     self.name = name
    #     self.etim_class_id = etim_class_id
    #     self.node_id = node_id
    #     self.id = id
