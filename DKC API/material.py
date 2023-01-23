from dataclasses import dataclass
from typing import List


@dataclass
class Certificate:
    id: int | None = None,
    name: str | None = None,
    src: str | None = None,
    type: str | None = None,
    number: str | None = None,
    start_date: int | None = None,
    expiration_date: int | None = None,
    node_ids: List[int] | None = None,
    item_ids: List[int] | None = None,
    item_full_codes: List[str] | None = None,


@dataclass
class Video:
    url: str | None = None,
    cover: str | None = None,
    type: str | None = None,


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


@dataclass
class MaterialRecord:
    material: Material | None = None
    certificates: List[Certificate] | None = None
    videos: List[Video] | None = None


def create_material_record(
        material_data: dict,
        material_certificates: List[dict],
        material_videos: List[dict],
) -> MaterialRecord:
    # material_object.pop('sale') # test unpacking
    record = MaterialRecord()
    record.material = Material(**material_data)
    record.certificates = [Certificate(**material_certificate) for material_certificate in material_certificates]
    record.videos = [Video(**material_video) for material_video in material_videos]
    return record
