# write your code here
import sys
from datetime import datetime
import os

STOP_COMMAND = "stop"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_argv(args: list) -> tuple[str, str]:
    dir_path = []
    file_name = ""
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "-d"
            continue

        if arg == "-f":
            mode = "-f"
            continue

        if mode == "-d":
            dir_path.append(arg)

        if mode == "-f":
            file_name = arg

    dir_path = os.path.join(*dir_path) if dir_path else ""
    return dir_path, file_name


def make_file() -> None:
    time_stamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    dir_path, file_name = parse_argv(sys.argv[1:])

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if not file_name:
        return

    file_path = os.path.join(dir_path, file_name)
    needs_separator = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as f:
        if needs_separator:
            f.seek(-1, 2)
            last_byte = f.read(1)
            if last_byte == "\n":
                f.write("\n")
            else:
                f.write("\n\n")
        f.write(f"{time_stamp}\n")
        i = 1
        while True:
            value = input("Enter content line: ")

            if value == STOP_COMMAND:
                break

            f.write(f"{i} {value}\n")
            i += 1


if __name__ == "__main__":
    make_file()
