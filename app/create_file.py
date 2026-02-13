import os
import datetime
import sys
import io

ARGS = sys.argv


def write_message(file_to_create: io.TextIOBase) -> None:
    file_to_create.write(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    )
    counter = 1
    while True:
        message = input("Enter content line: ")
        if message == "stop":
            break
        file_to_create.write(f"{counter} {message}\n")
        counter += 1


def create_file(args: list | tuple = ARGS) -> None:
    if "-f" in args:
        try:
            paths = os.path.join(*args[2:args.index("-f")])
            os.makedirs(paths, exist_ok=True)
        except Exception:
            paths = ""
        file_name = os.path.join(paths, args[-1])
        with open(file_name, "a") as file:
            if os.path.getsize(file_name):
                file.write(f"\n")
            write_message(file)
    else:
        paths = os.path.join(*args[2:])
        os.makedirs(paths, exist_ok=True)


if __name__ == "__main__":
    create_file()
