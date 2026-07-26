from sys import argv
from os import makedirs, path
from datetime import datetime


def make_directory(*arg) -> None | str:
    if not path.exists(str(path.join(*arg))):
        makedirs(path.join(*arg))
        return str(path.join(*arg))
    return str(path.join(*arg))


def create_file(name: str, time: str) -> None:
    if path.exists(name):
        with open(name, "a") as f:
            f.write(f"\n{time}\n")
            values = input("Enter content line: ")
            while values != "stop":
                f.write(f"{values}\n")
                values = input("Enter content line: ")
    else:
        with open(name, "w") as f:
            f.write(f"{time}\n")
            line = 1
            values = input("Enter content line: ")
            while values != "stop":
                f.write(f"{line} {values}\n")
                line += 1
                values = input("Enter content line: ")


def main() -> None:

    time = datetime.now().strftime("%Y-%m-%d %X")
    arguments = argv[1:]
    if "-f" not in arguments:
        make_directory(*arguments[1:])

    elif "-d" not in arguments:
        create_file(arguments[-1], time)

    else:
        d_position = arguments.index("-d")
        f_position = arguments.index("-f")
        if d_position < f_position:
            create_file(path.join(make_directory(
                *arguments[d_position + 1: f_position]),
                arguments[-1]), time)
        else:
            create_file(path.join(make_directory(*arguments[d_position + 1:]),
                                  arguments[f_position + 1]), time)


if __name__ == "__main__":
    main()
