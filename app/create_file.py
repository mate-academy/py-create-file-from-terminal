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


def create_path_regard_status(*flag_status: bool) -> str:
    f_flag_status, d_flag_status = flag_status
    path = ""
    if all(flag_status):
        first_dir = sys.argv.index("-d") + 1
        last_dir = sys.argv.index("-f")
        directories = sys.argv[first_dir:last_dir]
        path = os.path.join(*directories)

    if d_flag_status and not f_flag_status:
        directories = sys.argv[sys.argv.index("-d") + 1:]
        path = os.path.join(*directories)

    return path


def main():
    arguments = sys.argv[1:]
    flag_f = "-f" in arguments
    flag_d = "-d" in arguments

    if flag_f and not flag_d:
        filename = arguments[-1]
        file_mode = "w" if not os.path.exists(filename) else "a"
        write_content_to_file(filename, file_mode)

    if flag_d and not flag_f:
        new_path = create_path_regard_status(flag_f, flag_d)
        os.makedirs(new_path, exist_ok=True)

    if flag_f and flag_d:
        new_path = create_path_regard_status(flag_f, flag_d)
        os.makedirs(new_path, exist_ok=True)
        path_to_file = os.path.join(new_path, arguments[-1])
        file_mode = "w" if not os.path.exists(path_to_file) else "a"
        write_content_to_file(path_to_file, file_mode)


if __name__ == "__main__":
    main()
