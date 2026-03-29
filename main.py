

def menu():
    print("\n📋 TO-DO LIST")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Edytuj zadanie")
    print("4. Pokaż zadania")
    print("5. Filtruj zadania")
    print("6. Zapisz")
    print("7. Wyjdź")


def main():

    while True:
        menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Podaj zadanie: ")

        elif choice == "2":
            print("Podaj numer zadania: ")

        elif choice == "3":
            print("Podaj numer zadania: ")
            print("Nowa treść: ")
        elif choice == "4":
            print("Show tasks")

        elif choice == "5":
            print("done / undone: ")

        elif choice == "6":
            print("Zapisano!")

        elif choice == "7":
            break

        else:
            print("Nieprawidłowa opcja")


if __name__ == "__main__":
    main()