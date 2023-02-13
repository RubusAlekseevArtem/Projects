from dataclasses import dataclass, is_dataclass, asdict
from json import JSONEncoder
from typing import List

from DKC_API.data_classes.certificate import Certificate
from DKC_API.data_classes.material import Material
from DKC_API.data_classes.stock import Stock
from DKC_API.data_classes.video import Video


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


class MaterialRecordEncoder(JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)
