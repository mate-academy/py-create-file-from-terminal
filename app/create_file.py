from datetime import datetime
import os
from sys import argv


def create_file(path_with_file: str) -> None:
    with open(os.path.join(path_with_file), "a") as file:
        content = ""
        enumerate_line = 1
        while True:
            line = str(input("Enter content line: "))
            if line == "stop":
                break
            content += f"{enumerate_line} {line}\n"
            enumerate_line += 1
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(content)


def create_path(path_to_create: list) -> str:
    return os.path.join(*path_to_create)


def check_for_flags() -> None:
    if "-f" in argv and "-d" in argv:
        path = []
        for arg in argv[2:]:
            if arg == "-f":
                break
            path.append(arg)
        if not os.path.exists(create_path(path)):
            os.makedirs(create_path(path))
        path.append(argv[-1])
        create_file(create_path(path))

    elif argv[1] == "-d":
        path = create_path(argv[2:])
        os.makedirs(path)

    elif argv[1] == "-f":
        create_file(argv[2])


if __name__ == "__main__":
    check_for_flags()

