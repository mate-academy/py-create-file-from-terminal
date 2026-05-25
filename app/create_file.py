import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"{timestamp}\n"

    for index, line in enumerate(lines, start=1):
        content += f"{index} {line}\n"

    with open(file_path, "a", encoding="utf-8") as file:
        if file.tell() > 0:
            file.write("\n")

        file.write(content)


def main() -> None:
    args = sys.argv[1:]

    path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                dirs = args[d_index + 1 : f_index]
            else:
                dirs = args[d_index + 1 :]
        else:
            dirs = args[d_index + 1 :]

        path = os.path.join(*dirs)

        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        lines = get_content()

        file_path = (
            os.path.join(path, file_name)
            if path
            else file_name
        )

        write_to_file(file_path, lines)


if __name__ in ("__main__", "<run_path>"):
    main()
