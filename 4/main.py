"""Main module"""

from manage import fst, snd, frd


def main():
    while True:
        print("\nМЕТОД QIM")
        print("1. Встроить сообщение")
        print("2. Извлечь сообщение")
        print("3. Исказить изображение (тест робастности)")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            fst()
        elif choice == "2":
            snd()

        elif choice == "3":
            frd()

        elif choice == "4":
            break
        else:
            print(ValueError("Неверный ввод"))


if __name__ == "__main__":
    main()
