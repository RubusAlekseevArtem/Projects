from dataclasses import dataclass
from typing import List

from data_classes.certificate import Certificate
from data_classes.material import Material
from data_classes.stock import Stock
from data_classes.video import Video


@dataclass
class MaterialRecord:
    material: Material | None = None
    certificates: List[Certificate] | None = None
    videos: List[Video] | None = None
    stock: Stock | None = None
    accessories: List[str] | None = None
    drawings_sketch: List[str] | None = None
    description: List[str] | None = None


def create_material_record(
        material_data: dict,
        material_certificates: List[dict],
        material_videos: List[dict],
        material_stock: dict,
        material_accessories: List[str],
        material_drawings_sketch: List[str],
        material_description: List[str],
) -> MaterialRecord:
    # material_data.pop('sale') # test unpacking
    record = MaterialRecord()
    record.material = Material(**material_data)
    record.certificates = [Certificate(**material_certificate) for material_certificate in material_certificates]
    record.videos = [Video(**material_video) for material_video in material_videos]
    record.stock = Stock(**material_stock)
    record.accessories = material_accessories
    record.drawings_sketch = material_drawings_sketch
    record.description = material_description
    return record
