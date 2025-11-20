import sys
import os
import datetime


def time_without_microsecond() -> str:
    return f"{datetime.datetime.now().replace(microsecond=0)}"


def create_dirs() -> str:
    path = "/".join(
        sys.argv[
            sys.argv.index("-d") + 1: len(sys.argv)
            if "-f" not in sys.argv else sys.argv.index("-f")
        ]
    )
    if not os.path.exists(path):
        os.makedirs(path)
    return path + "\\"


def create_file(path: str = "") -> None:
    path = path + sys.argv[sys.argv.index("-f") + 1]
    with open(path, "a" if os.path.exists(path) else "w") as f:
        i = 1
        f.seek(0)
        f.write(
            f"{time_without_microsecond()}\n"
            if not os.stat(path).st_size > 0
            else f"\n{time_without_microsecond()}\n"
        )
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            f.write(f"{i} {text}\n")
            i += 1


def act_command() -> None:
    if len(sys.argv) > 1:
        if not ("-f" in sys.argv and "-d" in sys.argv):
            if sys.argv[1] == "-f":
                create_file()
            elif sys.argv[1] == "-d":
                create_dirs()
        else:
            create_file(create_dirs())


if __name__ == "__main__":
    act_command()
