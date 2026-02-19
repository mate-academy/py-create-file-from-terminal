# write your code here
import sys
from datetime import datetime
from pathlib import Path

STOP_COMMAND = "stop"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_argv(args: list) -> list[Path, str]:
    dir_path = []
    file_name = ""
    mode = False

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

    dir_path = Path(*dir_path)
    return dir_path, file_name


def make_file() -> None:
    time_stamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    dir_path, file_name = parse_argv(sys.argv)

    dir_path.mkdir(parents=True, exist_ok=True)

    file_path = Path(dir_path, file_name)
    print(file_path)

    with open(file_path, "a") as f:
        f.write(f"{time_stamp}\n")
        i = 1
        while True:
            value = input("Enter content line: ")

            if value == STOP_COMMAND:
                f.write("\n")
                break

            f.write(f"{i} {value} \n")


if __name__ == "__main__":
    make_file()
