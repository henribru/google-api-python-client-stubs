from _typeshed import Incomplete

from ..discovery_cache import DISCOVERY_DOC_MAX_AGE as DISCOVERY_DOC_MAX_AGE
from . import base as base

LOGGER: Incomplete
NAMESPACE: str

class Cache(base.Cache):
    def __init__(self, max_age) -> None: ...
    def get(self, url): ...
    def set(self, url, content) -> None: ...

cache: Incomplete
