import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    nargs="*",
    default=[],
)
parser.add_argument(
    "-f",
    nargs="?",  # 0 или 1 аргумент
    const="file.txt",  # Если -f без значения, будет "file.txt"
)
args = parser.parse_args()

# Создаём папку, если указан -d
if args.d:
    path = os.path.join(*args.d)
    os.makedirs(path, exist_ok=True)
    print(f"Создана папка: {path}")

# Создаём файл, если указан -f
if args.f is not None:  # Проверяем, был ли передан -f (даже без значения)
    filename = args.f if args.f else "file.txt"  # Используем переданное имя или "file.txt"

    # Если есть -d, файл создаётся внутри папки
    file_path = os.path.join(*args.d, filename) if args.d else filename

    with open(file_path, "w", encoding="UTF-8") as file:
        file.write(datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        i = 1
        while True:
            print("Enter content line: ")
            string = input()
            if string == "stop":
                break
            file.write(f"{i} {string}\n")
            i += 1