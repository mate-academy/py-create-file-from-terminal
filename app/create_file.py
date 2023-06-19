import os
import sys
import datetime


def get_new_path(args: list) -> str:
    path_list = [name for name in args if name not in ["-d", "-f"]]
    dir_path = os.path.join(*path_list[:-1])
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(*path_list)


def create_file() -> None:
    args = sys.argv[1:]
    file_name = args[-1]

    if "-d" in args:
        file_name = get_new_path(args)

    with open(file_name, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content_to_write = f"{timestamp}\n"
        line_counter = 1
        while True:
            user_data = input("Enter content line (or 'stop' to finish):")
            if user_data == "stop":
                content_to_write += "\n"
                break
            content_to_write += f"{line_counter} {user_data}\n"
            line_counter += 1
        file.write(content_to_write)


if __name__ == "__main__":
    create_file()
