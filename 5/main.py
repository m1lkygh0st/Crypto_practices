"""Main module"""

from manage import fst, snd, frd


def main():
    while True:
        print("\nЦВЗ")
        print("1) Встроить ЦВЗ и показать оценку")
        print("2) Извлечь ЦВЗ")
        print("3) Провести эксперименты – оценка робастности и атак")
        print("4) Выход")

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
            print(ValueError("Введите 1-4"))


if __name__ == "__main__":
    main()
