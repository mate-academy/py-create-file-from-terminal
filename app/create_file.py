import os
import sys
from datetime import datetime


def create_directory(parts: list) -> str:
    path = os.path.join(*parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        file.write(date)

        for line in iter(input, "stop"):
            file.write(line + "\n")
        file.write("\n")


def main() -> None:
    cmd_args = sys.argv
    d_index = cmd_args.index("-d") if "-d" in cmd_args else False
    f_index = cmd_args.index("-f") if "-f" in cmd_args else False

    if d_index:
        path = create_directory(cmd_args[d_index + 1:f_index]
                                if f_index > d_index
                                else cmd_args[d_index + 1:])
        if f_index:
            file_name = cmd_args[f_index + 1]
            create_file(file_name, path)


if __name__ == "__main__":
    main()
