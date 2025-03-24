import os
import datetime


def write_line_by_line(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            line_of_content = input("Enter content line: ")
            if line_of_content == "stop":
                break
            file.write(line_of_content + "\n")


def make_dirs_and_file(dirs_list: list, file_name: str = None) -> None:
    path = os.path.join(*dirs_list)
    os.makedirs(path, exist_ok=True)

    if file_name:
        write_line_by_line(os.path.join(path, file_name))


if __name__ == "__main__":
    write_line_by_line("test.txt")
