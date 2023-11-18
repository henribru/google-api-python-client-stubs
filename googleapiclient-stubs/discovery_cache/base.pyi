import abc

class Cache(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def get(self, url): ...
    @abc.abstractmethod
    def set(self, url, content): ...
