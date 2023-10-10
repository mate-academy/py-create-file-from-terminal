import os
import sys
import datetime


def get_info_from_terminal() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_directories()
        create_file(path)

    if "-d" in sys.argv:
        create_directories()

    if "-f" in sys.argv:
        path = []
        create_file(path)


def create_file(directories: list) -> None:

    name = sys.argv[sys.argv.index("-f") + 1]

    if len(directories) != 0:
        filename = os.path.join(*directories, name)
    else:
        filename = name

    with open(filename, "a") as file:
        content_data = []
        datetime_x = datetime.datetime.now()
        datetime_str = datetime_x.strftime("%Y-%m-%d %H:%M:%S")

        while True:
            data = input("Enter new line of content: ")
            if data == "stop":
                break
            content_data.append(data)

        file.write(f"{datetime_str}\n")
        for line_number, content in enumerate(content_data, 1):
            file.write(f"{line_number} {content}\n")
        file.write("\n")


def create_directories() -> list:
    d_index = sys.argv.index("-d")

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        directories = sys.argv[d_index + 1:f_index]
    else:
        directories = sys.argv[d_index + 1]

    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return directories


if __name__ == "__main__":
    get_info_from_terminal()
