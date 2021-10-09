from typing import Any

LOGGER: Any
DISCOVERY_DOC_MAX_AGE: Any
DISCOVERY_DOC_DIR: Any

def autodetect(): ...
def get_static_doc(serviceName, version): ...
