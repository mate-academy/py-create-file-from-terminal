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
        while True:
            content = input("Enter content line: ") + "\n"
            if content == "stop\n":
                break
            file.write(content)
        file.write("\n")


def main() -> None:
    cmd_args = sys.argv
    print(cmd_args)
    if "-f" in cmd_args and "-d" in cmd_args:
        path = create_directory(
            cmd_args[cmd_args.index("-d") + 1:cmd_args.index("-f")]
        )
        file_name = cmd_args[cmd_args.index("-f") + 1]
        create_file(file_name, path)

    elif "-d" in cmd_args:
        create_directory(cmd_args[cmd_args.index("-d") + 1:])

    elif "-f" in cmd_args:
        create_file(cmd_args[cmd_args.index("-f") + 1])


if __name__ == "__main__":
    main()
