from dataclasses import dataclass
from typing import List


@dataclass
class Material:
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
    thumbnail_url: str | None = None,
    additional_images: List[str] | None = None,
    attributes: dict | None = None,
    etim_attributes: dict | None = None,
    packing: dict | None = None,
    avg_delivery: dict | None = None,
    accessories: List[str] | None = None,
    accessories_codes: List[str] | None = None,
    sale: List | None = None,
