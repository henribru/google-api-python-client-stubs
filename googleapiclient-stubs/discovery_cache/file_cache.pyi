from typing import Any

from ..discovery_cache import DISCOVERY_DOC_MAX_AGE as DISCOVERY_DOC_MAX_AGE
from . import base as base

LOGGER: Any
FILENAME: str
EPOCH: Any

class Cache(base.Cache):
    def __init__(self, max_age: Any) -> None: ...
    def get(self, url: Any): ...
    def set(self, url: Any, content: Any) -> None: ...

cache: Any
