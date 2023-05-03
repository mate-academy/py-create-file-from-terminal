import datetime
import os
import sys


def parsing_parameters() -> tuple:
    directories = []
    full_file_name = ""
    if "-f" in sys.argv and "-d" in sys.argv:
        full_file_name = sys.argv[sys.argv.index("-f") + 1]
        directories = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
    elif "-f" in sys.argv:
        full_file_name = sys.argv[sys.argv.index("-f") + 1]
    elif "-d" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:]
    else:
        pass
    return directories, full_file_name


def make_directories(directories_list: list) -> str:
    directories_path = ""
    if len(directories_list) > 0:
        directories_path = "/".join(directories_list)
        os.makedirs(directories_path, exist_ok=True)
        directories_path += "/"
    return directories_path


def create_file_with_content(content_path: str, name: str) -> None:
    file_exists = os.path.exists(content_path + name)
    if len(name) > 0:
        with open(content_path + name, "a") as file:
            # add current timestamp
            time_format = "%Y-%m-%d %H:%M:%S"
            file.write(
                ("\n" if file_exists else "")
                + str(datetime.datetime.now().strftime(time_format))
                + "\n"
            )

            # add content lines
            content = None
            row_number = 1
            while content != "stop":
                content = input("Enter content line: ")
                if content != "stop" and content is not None:
                    file.write(str(row_number) + " " + content + "\n")
                    row_number += 1


if __name__ == "__main__":
    dirs_list, file_name = parsing_parameters()
    path = make_directories(dirs_list)
    create_file_with_content(path, file_name)
