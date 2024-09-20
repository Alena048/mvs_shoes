from model.model import Model
from vies.ConsoleVies import ConsoleVies
from controler.controler import ConsolControler
from Shoes import Shoes


def main():
    model = Model()
    vies = ConsoleVies()
    contr = ConsolControler(
        model=model,
        vies=vies
    )

    while True:
        user_input = input("Действие, которое необходимо сделать: \n"
                           "1 - Добавить пару обуви \n"
                           "2 - Показать весь каталог обуви \n"
                           "3 - Удалить пару обуви \n"
                           "4 - Поиск пары обуви \n"
                           "5 - Замена цены обуви\n"
                           "6 - Выход \n")
        if user_input == "1":
            contr.save_shoes()
        if user_input == "2":
            contr.get_all_shoes()
        if user_input == "3":
            contr.dell_shoes()
        if user_input == "4":
            contr.search_shoes()
        if user_input == "5":
            contr.replace()
        if user_input == "6":
            break

if __name__ == '__main__':
    main()