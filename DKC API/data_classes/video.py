from dataclasses import dataclass


@dataclass
class Video:
    url: str | None = None,
    cover: str | None = None,
    type: str | None = None,
