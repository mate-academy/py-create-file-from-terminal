import sys
import os
from datetime import datetime


def get_content() -> list[str]:
    lines = []
    count = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{count} {line}")
        count += 1

    return lines


def create_directories(dirs: list[str]) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")  # пустая строка между записями

        f.write(f"{timestamp}\n")
        for line in content:
            f.write(f"{line}\n")


def main() -> None:
    args = sys.argv[1:]

    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        # берем все аргументы после -d до -f (если есть)
        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    # создаем путь
    base_path = ""
    if dirs:
        base_path = create_directories(dirs)

    # если указан файл
    if file_name:
        file_path = (
            os.path.join(base_path, file_name)
            if base_path
            else file_name
        )

        content = get_content()
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
