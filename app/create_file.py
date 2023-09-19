import os
import sys
from datetime import datetime


def create_dir(parts_of_path: list) -> str:
    path = os.path.join(*parts_of_path)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        file.write(date)
        while True:
            content = input("Write content: ") + "\n"
            if content == "stop\n":
                break
            file.write(content)
        file.write("\n")


def main() -> None:
    if "-f" in sys.argv and "-d" in sys.argv:
        path = create_dir(
            sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        )
        file_name = sys.argv[sys.argv.index("-f") + 1]
        create_file(file_name, path)

    elif "-d" in sys.argv:
        create_dir(sys.argv[sys.argv.index("-d") + 1:])

    elif "-f" in sys.argv:
        create_file(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    main()
