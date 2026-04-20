import os


def create_file_or_directory(args: list[str]) -> None:
    # Перевірка наявності хоча б одного прапорця -d або -f
    if "-d" not in args and "-f" not in args:
        print("Помилка: необхідно вказати хоча б один з прапорців: -d або -f")
        return

    # Перевірка наявності шляху до каталогу, якщо передано -d
    directory_path = ""
    if "-d" in args:
        f_index = args.index("-d")
        if len(args) > f_index + 1:
            directory_path = args[f_index + 1]
        else:
            print("Помилка: не вказано шлях до каталогу після -d.")
            return

        # Перевірка шляху до каталогу
        if not os.path.exists(directory_path):
            print(f"Помилка: каталог {directory_path} не існує.")
            return

        # Створення каталогу (якщо потрібно)
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Каталог {directory_path} успішно створений.")
        except PermissionError:
            print(f"Помилка: недостатньо прав для створення каталогу "
                  f"{directory_path}.")
            return

    # Обробка введення користувачем
    try:
        print("Введіть рядки вмісту. Введіть 'stop' для завершення.")
        content = []
        while True:
            line = input("Введіть рядок вмісту: ")
            if line == "stop":
                break
            content.append(line)

        # Якщо вказано створення файлу
        if "-f" in args:
            f_index = args.index("-f")
            if len(args) > f_index + 1:
                file_name = args[f_index + 1]
                # Створення файлу та запис вмісту
                with open(file_name, "w") as file:
                    file.write("\n".join(content))
                print(f"Файл {file_name} успішно створений.")
            else:
                print("Помилка: не вказано ім'я файлу після -f.")
                return

    except EOFError:
        print("\nПомилка: кінець файлу (EOF).")
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")
