import sys
import os
from datetime import datetime

args = sys.argv[1:]

dirs = []
file_name = None

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        while i < len(args) and not args[i].startswith("-"):
            dirs.append(args[i])
            i += 1
    elif args[i] == "-f":
        i += 1
        if i < len(args) and not args[i].startswith("-"):
            file_name = args[i]
            i += 1
    else:
        i += 1

target_dir = "."
if "-d" in args:
    if dirs:
        target_dir = os.path.join(*dirs)
        os.makedirs(target_dir, exist_ok=True)

# 2. Створення файлу та запис
if "-f" in args and file_name:
    file_path = os.path.join(target_dir, file_name)

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)
        except EOFError:
            break

    # Формуємо блок тексту для цього запуску
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_to_write = f"{current_time}\n"
    for idx, line in enumerate(lines, start=1):
        content_to_write += f"{idx} {line}\n"

    prefix = ""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        prefix = "\n"
        # Записуємо у файл
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(prefix + content_to_write)
