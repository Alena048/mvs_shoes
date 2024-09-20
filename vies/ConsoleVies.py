from vies.IVies import IVies
from Shoes import Shoes


class ConsoleVies(IVies):
    def get_shoes(self, mes_id: str = "Введите уникальный номер пары обуви \n",
                        mes_type: str = "Введите тип обуви: МУЖ или ЖЕН \n ",
                        mes_model: str = "Введите модель обуви: \n",
                        mes_color: str = "Введите цвет обуви: \n",
                        mes_price: str = "Введите цену обуви: \n",
                        mes_manufacturer: str = "Введите производителя: \n",
                        mes_size: str = "Введите размер обуви: \n") -> Shoes:
        id = input(mes_id)
        type = input(mes_type)
        model = input(mes_model)
        color = input(mes_color)
        price = input(mes_price)
        manufacturer = input(mes_manufacturer)
        size = input(mes_size)
        return Shoes(
            id=id,
            type=type,
            model=model,
            color=color,
            price=price,
            manufacturer=manufacturer,
            size=size
        )

    def dell_shoes(self, mes: str = "Введите id пары обуви для удаления: \n") -> str:
        return input(mes)

    def print_all_shoes(self, shoess: list[Shoes]):
        for shoes in shoess:
            print(shoes)
            print("*" * 40)

    def search_shoes(self, mes_name: str = "Введите id пары обуви для поиска: \n") -> str:
        return input(mes_name)

    def replace(self, mes_name: str = "Введите id пары обуви для поиска: \n",
                      new_price: str = "Введите новую цену: \n"):
        return input(mes_name), input(new_price)



