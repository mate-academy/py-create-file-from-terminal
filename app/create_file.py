import sys
import os
from datetime import datetime

args = sys.argv[1:]

dir_path = []
file_name = None

# Обробка прапора -d (шлях до директорії)
if "-d" in args:
    d_index = args.index("-d")
    for item in args[d_index + 1:]:
        if item in ["-f", "-d"]:
            break
        dir_path.append(item)

# Обробка прапора -f (ім’я файлу)
if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        file_name = args[f_index + 1]

# Створення директорії, якщо вказано
if dir_path:
    os.makedirs(os.path.join(*dir_path), exist_ok=True)

# Якщо не вказано файл, завершити
if not file_name:
    print("Помилка: не вказано ім’я файлу. Використайте прапор -f.")
    sys.exit(1)

# Побудова повного шляху до файлу
full_path = os.path.join(*dir_path, file_name) if dir_path else file_name

# Ввід вмісту
lines = []
while True:
    line = input("Enter content line: ")
    if line.strip().lower() == "stop":
        break
    lines.append(line)

# Запис у файл
with open(full_path, "a", encoding="utf-8") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")
    f.write("\n")
