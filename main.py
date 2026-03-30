from tasks import TaskManager
from storage import save_tasks, load_tasks

def menu():
    print("\n📋 TO-DO LIST")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Edytuj nazwę zadania")
    print("4. Pokaż zadania")
    print("5. Filtruj zadania")
    print("6. Zapisz")
    print("7. Wyjdź")


def main():
    tasks = load_tasks()
    manager = TaskManager(tasks)

    while True:
        menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Podaj zadanie: ")
            manager.add_task(title)
            
        elif choice == "2":
            manager.show_tasks()
            index = int(input("Podaj numer zadania: "))
            manager.delete_task(index)

        elif choice == "3":
            manager.show_tasks()
            index = int(input("Podaj numer zadania: "))
            new_title = input("Nowa teść: ")
            manager.edit_task(index, new_title)
            
        elif choice == "4":
            manager.show_tasks()

        elif choice == "5":
            status = input("zrobione / niezrobione: ")
            manager.filter_tasks(status)

        elif choice == "6":
            save_tasks(manager.tasks)
            print("Zapisano!")

        elif choice == "7":
            save_tasks(manager.tasks)
            break

        else:
            print("Nieprawidłowa opcja")


if __name__ == "__main__":
    main()