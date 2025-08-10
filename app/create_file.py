import os
import sys
import datetime


def time_stamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_file(file_name: str, directories: list[str]) -> str:
    if len(directories) > 0:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, file_name)
    else:
        file_path = os.path.join(file_name)
    open(file_path, "a")
    return file_path


def create_content(file_path: str) -> None:
    next_input = ""
    line_number = 1
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n" + time_stamp() + "\n")
        else:
            f.write(time_stamp() + "\n")
        while next_input != "stop":
            next_input = input("Enter new line of content: ")
            if next_input == "stop":
                break
            f.write(f"{line_number} {next_input}\n")
            line_number += 1


def main() -> None:
    argv = sys.argv

    directories = []
    if "-d" in argv:
        for dir_index in range(argv.index("-d") + 1, len(argv)):
            if argv[dir_index] == "-f":
                break
            directories.append(argv[dir_index])
            path = os.path.join(*directories)
            os.makedirs(path, exist_ok=True)
    if "-f" in argv:
        path = create_file(argv[-1], directories)
        create_content(path)


if __name__ == "__main__":
    main()
