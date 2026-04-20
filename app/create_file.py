import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Package {path} ...")


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Enter content line(type stop to finish)")
    content_line = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_line.append(line)

    if not content_line:
        print("Файл не був оновлений, оскільки не введено жодного рядка")
        return

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for index, line in enumerate(content_line, start=1):
            file.write(f"{index} {line}\n")
    print(f"Вміст данного файлу {file_path}.")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [directory] -f [filename]")
        return

    directory = ""
    filename = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directory = os.path.join(*args[d_index + 1:f_index])
        else:
            directory = os.path.join(*args[d_index + 1:])
            create_directory(directory)
            return

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]
        else:
            print("Помилка: не вказано імя файлу після -f.")
            return

    if not filename:
        print("Помилка: не вказано імя файлу.")
        return

    file_path = os.path.join(directory, filename) if directory else filename

    if directory:
        create_directory(directory)

    write_to_file(file_path)


if __name__ == "__main__":
    main()
