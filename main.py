import zoo

def main():
    my_zoo = zoo.Zoo()
    while True:
        print("1 - Информация о зоопарке")
        print("2 - Добавить животное")
        print("3 - Добавить сотрудника")
        print("4 - Покормить животных")
        print("5 - Полечить животных")
        print("6 - Пугнуть всех")
        print("7 - Сохранить в файл")
        print("8 - Загрузить из файла")
        print("9 - Выход")
        answer = input("Выберите действие: ").strip()
        print()
        if answer == "1":
            my_zoo.show_all()
        if answer == "2":
            my_zoo.add_animal()
        if answer == "3":
            my_zoo.add_employee()
        if answer == "4":
            my_zoo.feed_animals()
        if answer == "5":
            my_zoo.treat_animals()
        if answer == "6":
            my_zoo.disturb_animals()
        if answer == "7":
            filename = input("Введите имя файла: ")
            my_zoo.save(filename)
        if answer == "8":
            filename = input("Введите имя файла: ")
            my_zoo.load(filename)
        if answer == "9":
            return

if __name__ == "__main__":
    main()