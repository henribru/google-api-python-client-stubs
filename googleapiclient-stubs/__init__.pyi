import logging

class NullHandler(logging.Handler):
    def emit(self, record) -> None: ...
