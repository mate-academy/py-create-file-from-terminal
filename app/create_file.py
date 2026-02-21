import os
from datetime import datetime
from sys import argv


args = argv[1:]

directory_parts = []
filename = None
path = None

if "-d" in args:
    d_index = args.index("-d") + 1
    while d_index < len(args) and not args[d_index].startswith("-"):
        directory_parts.append(args[d_index])
        d_index += 1

if "-f" in args:
    f_index = args.index("-f") + 1
    if f_index < len(args):
        filename = args[f_index]

if "-f" not in args or not filename:
    print("❌ Помилка: Потрібно вказати ім'я файлу з прапорцем -f.")
    print("▶ Приклад: python create_file.py -f file.txt")
    print("▶ Або:     python create_file.py -d dir1 dir2 -f file.txt")
    exit(1)

if directory_parts:
    path = os.path.join(*directory_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")

if filename:
    if path:
        file_path = os.path.join(path, filename)
    else:
        file_path = filename

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = timestamp + "\n"
    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content + "\n")
