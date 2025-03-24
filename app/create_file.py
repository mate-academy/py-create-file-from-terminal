import sys
import os
from datetime import datetime


def create_directory(path):
    os.makedirs(path, exist_ok=True)
    print(f"Директорію '{path}' створено (або вона вже існує).")


def write_to_file(file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []
    count = 1
    print("Введіть вміст файлу (введіть 'stop' для завершення):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{count} {line}")
        count += 1

    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(f"{timestamp}\n")
        f.write("\n".join(content_lines) + "\n")
    print(f"Файл '{file_path}' оновлено.")


def main():
    args = sys.argv[1:]
    if not args:
        print("Будь ласка, передайте аргументи: -d для директорії, -f для файлу.")
        return

    dir_path = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
            break
        else:
            print(f"Невідомий аргумент: {args[i]}")
            return

    if dir_path:
        full_dir_path = os.path.join(os.getcwd(), *dir_path)
        create_directory(full_dir_path)
    else:
        full_dir_path = os.getcwd()

    if file_name:
        file_path = os.path.join(full_dir_path, file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    main()
