import os
import sys
from datetime import datetime


def create_file(directory_path: str,
                file_name: str) -> None:
    with open(os.path.join(directory_path, file_name), "a") as file:
        file.write(
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        number_line = 1

        while True:
            record_info = input("Enter content line: ")
            if record_info.lower() == "stop":
                file.write("\n\n")
                break
            file.write(
                f"\n{number_line} {record_info}"
            )
            number_line += 1


def create_dir(path_l : list) -> str:
    path = os.path.join(*path_l)
    os.makedirs(path, exist_ok=True)
    return path


def main() -> None:
    argv = sys.argv
    if "-d" in argv and "-f" not in argv:
        create_dir(argv[argv.index("-d") + 1:])

    elif "-f" in argv and "-d" in argv:
        if argv.index("-f") > argv.index("-d"):
            path = create_dir(argv[argv.index("-d") + 1:
                                   argv.index("-f")])
        else:
            path = create_dir(argv[argv.index("-d") + 1:])
        name = argv[argv.index("-f") + 1]
        create_file(path, name)

    elif "-f" in argv and "-d" not in argv:
        name = argv[argv.index("-f") + 1]
        create_file("", name)


if __name__ == "__main__":
    main()
