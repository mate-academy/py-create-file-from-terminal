import sys
import os
from datetime import datetime


# Функція створюе директорію за вказанним path
def create_dir(path: str) -> None:
    if isinstance(path, str):
        os.makedirs(path, exist_ok=True)


def create_file(
    file_name: str,
    file_content: str,
    directory: str = ""
) -> None:
    curent_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = file_content.splitlines()
    numbered_lines = [f"{i} {line}" for i, line in enumerate(lines, start=1)]
    str_to_file = curent_date + "\n" + "\n".join(numbered_lines)
    file_path = os.path.join(directory, file_name) if directory else file_name
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        str_to_file = "\n\n" + str_to_file
    with open(f"{file_path}", "a") as file:
        file.write(str_to_file)


# Перевіряємо чи вказаний аргумент -d
if "-d" in sys.argv:
    start = sys.argv.index("-d") + 1

    # 2. Шукаєм -f, але тільки ЯКЩО він іде ПІСЛЯ -d
    # Створюємо окремий список всього що іде після -d
    after_d = sys.argv[start:]

    if "-f" in after_d:
        end_relative = after_d.index("-f")
        dirs_list = after_d[:end_relative]
    else:
        # Якщо -f немає (або він був раніше), берем все до кінця
        dirs_list = after_d

    # 3. В str
    dir_path = os.path.join(*dirs_list)
    create_dir(dir_path, exist_ok=True)
else:
    dir_path = ""

# Перевіряємо чи вказаний аргумент -f
if "-f" in sys.argv:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    if file_name:
        text_lines = ""
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            text_lines += input_line + "\n"
        text_lines = text_lines.rstrip("\n")
        create_file(file_name, text_lines, dir_path)
