import sys
import os
from datetime import datetime


args = sys.argv

# Извлекаем директории
directories = []
if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1:f_index]
    else:
        directories = args[d_index + 1:]
    # Создаём папки
    os.makedirs(os.path.join(*directories), exist_ok=True)

# Извлекаем имя файла и работаем с контентом
if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    # Собираем контент
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    # Форматируем контент
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"
    for i, line in enumerate(lines, start=1):
        content += f"{i} {line}\n"

    # Определяем путь
    if directories:
        file_path = os.path.join(*directories, file_name)
    else:
        file_path = file_name

    # Записываем файл
    with open(file_path, "a") as output_file:
        output_file.write(content + "\n")
