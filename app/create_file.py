import sys
import os
from datetime import datetime


def main() -> None:
    datas = sys.argv[1:]
    path_directs = "."
    name = ""
    if "-d" in datas:
        d_index = datas.index("-d")
        if "-f" in datas:
            f_index = datas.index("-f")
            dir_parts = datas[d_index + 1:f_index]
        else:
            dir_parts = datas[d_index + 1:]
        path_directs = os.path.join(*dir_parts)
        os.makedirs(path_directs, exist_ok=True)

    if "-f" in datas:
        f_index = datas.index("-f")
        try:
            name = datas[f_index + 1]
        except IndexError:
            return
    file_path = os.path.join(*path_directs, name)

    lines = []
    while True:
        line = input("Enter the line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_path, "a",) as file:
        set_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{set_time}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


if __name__ == "__main__":
    main()
