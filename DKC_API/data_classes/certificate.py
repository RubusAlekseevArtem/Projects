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
