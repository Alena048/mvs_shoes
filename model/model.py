from model.imodel import IModel
from Shoes import Shoes


_DB: list[Shoes] = []


class Model(IModel):
    def save_shoes(self, shoes: Shoes):
        _DB.append(shoes)

    def dell_shoes(self, id_shoes: str):
        for i in range(len(_DB)):
            if _DB[i].id == id_shoes:
                _DB.pop(i)
                return

    def get_all_shoes(self) -> list[Shoes]:
        return _DB

    def search_shoes(self, id_shoes: str):
        for i in range(len(_DB)):
            if _DB[i].id == id_shoes:
                return print(_DB[i])
        else:
            print("Нет обуви соотвествующей данному id номеру")


    def replace(self, id_shoes: str, new_price: str):
        for i in range(len(_DB)):
            if _DB[i].id == id_shoes:
                _DB[i].price = new_price
                return print(_DB[i])

