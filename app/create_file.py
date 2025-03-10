import sys
import os
from datetime import datetime


def create_file_or_directory(args: list[str]) -> None:
    """Створює файл або каталог на основі аргументів командного рядка."""
    directory_path = None
    file_name = None
    content_lines = []

    # Розбираємо аргументи вручну
    if "-d" in args:
        d_index = args.index("-d")
        # Перевіряємо, чи після -d є хоч один каталог
        if d_index + 1 >= len(args) or args[d_index + 1] in ["-f", "-d"]:
            print("Помилка: після '-d' повинен бути шлях до каталогу.")
            return
        # Збираємо всі частини шляху після -d
        # до наступного прапора (-f або нового -d)
        next_flag = next(
            (i for i, arg in enumerate(args[d_index + 1:], start=d_index + 1)
             if arg in ["-f", "-d"]), len(args)
        )
        directory_path = os.path.join(*args[d_index + 1:next_flag])

    if "-f" in args:
        f_index = args.index("-f")
        # Перевіряємо, чи після -f є ім'я файлу
        if f_index + 1 >= len(args) or args[f_index + 1] in ["-d", "-f"]:
            print("Помилка: після '-f' повинно бути ім'я файлу.")
            return
        file_name = args[f_index + 1]

    # Якщо передано -d, створюємо каталог
    if directory_path:
        try:
            os.makedirs(directory_path, exist_ok=True)
        except OSError as e:
            print(f"Помилка створення каталогу: {e}")
            return

    # Якщо передано -f, створюємо файл
    if file_name:
        file_path = os.path.join(directory_path, file_name) \
            if directory_path else file_name

        # Визначаємо режим запису
        file_exists = os.path.exists(file_path)
        mode = "a" if file_exists else "w"

        print("Введіть рядки вмісту. Введіть 'stop' для завершення.")
        line_number = 1
        while True:
            line = input("Введіть рядок вмісту: ")
            if line.lower() == "stop":
                break
            content_lines.append(f"{line_number} {line}")
            line_number += 1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_path, mode, encoding="utf-8") as f:
                if file_exists and os.path.getsize(file_path) > 0:
                    f.write("\n\n")  # Додаємо два порожніх рядки між записами
                f.write(timestamp + "\n")
                f.write("\n".join(content_lines) + "\n")

        except OSError as e:
            print(f"Помилка запису у файл: {e}")
            return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python create_file.py [-d <каталог>] [-f <файл>]")
    else:
        create_file_or_directory(sys.argv)
