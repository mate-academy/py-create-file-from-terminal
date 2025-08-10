import os

import datetime

import sys


def write_content_to_file(filepath: str, mode: str) -> None:
    with open(filepath, mode) as file_in:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_in.write(f"{time_now}\n")
        counter = 0
        while True:
            content = input("Enter content line: ")
            counter += 1
            if content == "stop":
                break

            file_in.write(f"{counter} {content}\n")


def create_path(directories: list[str], filename: str = "") -> str:
    return os.path.join(*directories, filename)


def main() -> None:
    flag_f = "-f" in sys.argv
    flag_d = "-d" in sys.argv

    if flag_f and not flag_d:
        file_mode = "w" if not os.path.exists(sys.argv[-1]) else "a"
        write_content_to_file(sys.argv[-1], file_mode)

    if flag_d and not flag_f:
        dir_names = sys.argv[sys.argv.index("-d") + 1:]
        os.makedirs(create_path(dir_names), exist_ok=True)

    if flag_f and flag_d:
        first_dir = sys.argv.index("-d") + 1
        last_dir = sys.argv.index("-f")
        os.makedirs(create_path(sys.argv[first_dir:last_dir]), exist_ok=True)
        write_content_to_file(
            create_path(sys.argv[first_dir:last_dir], sys.argv[-1]),
            "w"
        )


if __name__ == "__main__":
    main()
