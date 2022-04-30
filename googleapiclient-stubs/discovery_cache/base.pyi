import abc

from _typeshed import Incomplete

class Cache(metaclass=abc.ABCMeta):
    __metaclass__: Incomplete
    @abc.abstractmethod
    def get(self, url): ...
    @abc.abstractmethod
    def set(self, url, content): ...
