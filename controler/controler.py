from Shoes import Shoes
from model.imodel import IModel
from vies.IVies import IVies


class ConsolControler:
    def __init__(self, model: IModel, vies: IVies):
        self.model = model
        self.vies = vies

    def save_shoes(self):
        shoes = self.vies.get_shoes()
        self.model.save_shoes(shoes)

    def dell_shoes(self):
        id_shoes = self.vies.dell_shoes()
        self.model.dell_shoes(id_shoes)

    def get_all_shoes(self):
        shoess = self.model.get_all_shoes()
        self.vies.print_all_shoes(shoess)

    def search_shoes(self):
        id_shoes = self.vies.search_shoes()
        self.model.search_shoes(id_shoes)

    def replace(self):
        id_shoes, new_price = self.vies.replace()
        self.model.replace(id_shoes, new_price)

