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
