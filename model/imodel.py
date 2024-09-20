from Shoes import Shoes
from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def save_shoes(self, shoes: Shoes):
        pass

    @abstractmethod
    def dell_shoes(self, id_shoes: str):
        pass

    @abstractmethod
    def get_all_shoes(self) -> list[Shoes]:
        pass

    @abstractmethod
    def search_shoes(self, id_shoes: str):
        pass

    @abstractmethod
    def replace(self, id_shoes: str, new_price: str):
        pass