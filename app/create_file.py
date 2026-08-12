import sys
import os
from datetime import datetime


def main() -> None:
    args: list[str] = sys.argv[1:]

    dir_path: str = ""
    file_name: str = ""

    # 1. Розбираємо прапорець -d (незалежно від його позиції)
    if "-d" in args:
        d_index = args.index("-d")
        dir_parts: list[str] = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)

        if dir_parts:
            dir_path = os.sep.join(dir_parts)

    # 2. Розбираємо прапорець -f (незалежно від його позиції)
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    # 3. Створюємо папки, якщо вони вказані
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # 4. Якщо файл вказано — запитуємо текст та записуємо у файл
    if file_name:
        lines: list[str] = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        full_path: str = os.path.join(dir_path, file_name)\
            if dir_path else file_name
        timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(full_path, "a") as f:
            f.write(timestamp + "\n")
            for index, line_content in enumerate(lines, start=1):
                f.write(f"{index} {line_content}\n")


if __name__ == "__main__":
    main()
