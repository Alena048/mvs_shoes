from abc import ABC, abstractmethod
from Shoes import Shoes

class IVies(ABC):
    @abstractmethod
    def get_shoes(self) -> Shoes:
        pass

    @abstractmethod
    def print_all_shoes(self, shoess: list[Shoes]):
        pass

    @abstractmethod
    def dell_shoes(self) -> str:
        pass

    @abstractmethod
    def search_shoes(self) -> str:
        pass

    @abstractmethod
    def replace(self):
        pass
