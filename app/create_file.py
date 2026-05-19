import os
import sys
import datetime


def write_file(filename: str) -> None:
    with open(filename, "a", encoding="utf-8") as user_file:
        user_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        )
        line_counter = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                user_file.write("\n")
                return
            user_file.write(f"{line_counter} {user_input}\n")
            line_counter += 1


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        directory_path = sys.argv[d_index + 1:f_index]
        dir_path = os.path.join(*directory_path)
        os.makedirs(dir_path, exist_ok=True)
        file_path = sys.argv[f_index + 1]
        directory_path.append(file_path)
        full_file_path = os.path.join(*directory_path)
        write_file(full_file_path)
    elif "-d" in sys.argv and "-f" not in sys.argv:
        d_index = sys.argv.index("-d")
        directory = sys.argv[d_index + 1:]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        write_file(file_name)


if __name__ == "__main__":
    create_file()
