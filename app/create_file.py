import datetime
import os
import sys


def create_directories(path: list) -> str:
    if "f" in path:
        new_dir = os.path.join(path[2:-2])
    else:
        new_dir = os.path.join(path[2:])
    os.makedirs(new_dir)
    return new_dir


def create_file() -> None:
    path_list = sys.argv
    filename = path_list[-1]

    if "-d" in path_list:
        new_dir = create_directories(path_list)
        path_to_file = os.path.join(new_dir, filename)
    else:
        path_to_file = filename

    with open(path_to_file, "a") as f:
        current_time = datetime.datetime.now()
        time_file = current_time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(time_file + "\n")
        count_line = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content != "stop":
                f.write(f"{str(count_line)} {line_content}" + "\n")
                count_line += 1
            else:
                f.write("\n")
                break


if __name__ == "__main__":
    create_file()
