import sys
import os
from datetime import datetime

# Збираємо аргументи
args = sys.argv[1:]  # без назви скрипта

directories = []
file_name = None

# Шукаємо прапорці і визначаємо їх значення
if "-d" in args:
    d_index = args.index("-d")
    # Папки йдуть до наступного прапорця або до кінця
    next_flags = [i for i, arg in enumerate(args) if arg.startswith("-") and i != d_index]
    if next_flags:
        end_index = min([i for i in next_flags if i > d_index])
        directories = args[d_index + 1:end_index]
    else:
        directories = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 >= len(args):
        print("Помилка: після -f не вказано назву файлу.")
        sys.exit(1)
    file_name = args[f_index + 1]

# Створюємо шлях до директорій
dir_path = ""
if directories:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)

# Якщо вказано файл
if file_name:
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    # Зчитуємо рядки контенту від користувача
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    if not content_lines:
        print("Немає рядків для запису.")
        sys.exit(0)

    # Додаємо timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Формуємо текст для запису
    output_text = timestamp + "\n"
    for line_number, text_line in enumerate(content_lines, start=1):
        output_text += f"{line_number} {text_line}\n"
    output_text += "\n"

    # Записуємо у файл, додаючи новий контент в кінець
    with open(file_path, "a", encoding="utf-8") as file_obj:
        file_obj.write(output_text)

    print(f"Контент записано у файл: {file_path}")
