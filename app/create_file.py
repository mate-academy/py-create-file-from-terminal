import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""
    if not args:
        print("Укажи хотя бы -f или -d флаг.")
        return

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1:f_index]
        else:
            dir_parts = args[d_index + 1:]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Укажи имя файла после -f")
            return

    file_path = os.path.join(dir_path, file_name)

    print("\nВведите строки. Чтобы завершить — напиши 'stop'.\n")
    lines = []
    while True:
        line = input("Введите строку: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_path, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")

    print(f"\nФайл успешно обновлён: {file_path}")


if __name__ == "__main__":
    main()