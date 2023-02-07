from dataclasses import dataclass
from typing import List

from .data_classes.certificate import Certificate
from .data_classes.material import Material
from .data_classes.stock import Stock
from .data_classes.video import Video


@dataclass
class MaterialRecord:
    material: Material | None = None
    certificates: List[Certificate] | None = None
    stock: Stock | None = None
    related: List[str] | None = None
    accessories: List[str] | None = None
    videos: List[Video] | None = None
    drawings_sketch: List[str] | None = None
    description: List[str] | None = None
    analogs: List[str] | None = None
    specification: List[str] | None = None


def create_material_record(
        material: dict,
        material_certificates: List[dict],
        material_videos: List[dict],
        material_stock: dict,
        material_related: List[str],
        material_accessories: List[str],
        material_drawings_sketch: List[str],
        material_description: List[str],
        material_analogs: List[str],
        material_specification: List[str],
) -> MaterialRecord:
    # material_data.pop('sale') # test unpacking
    record = MaterialRecord()

    record.material = Material(**material)
    record.certificates = [Certificate(**material_certificate) for material_certificate in material_certificates]
    record.videos = [Video(**material_video) for material_video in material_videos]
    record.stock = Stock(**material_stock)
    record.related = material_related
    record.accessories = material_accessories
    record.drawings_sketch = material_drawings_sketch
    record.description = material_description
    record.analogs = material_analogs
    record.specification = material_specification

    return record
