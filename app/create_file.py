import datetime
import os.path
import sys


def get_directory_and_file(data: list[str]) -> tuple:
    """
    We receive data from the terminal and find directories and a file
    to write to. If there are no directories, then we set the value
    to False. If there is no final file, we write a string with
    the file name.
    """
    if "-d" not in data:
        directory_data = False
    elif "-d" in data and "-f" in data:
        directory_data = data[data.index("-d") + 1:data.index("-f")]
    else:
        directory_data = data[data.index("-d") + 1:]

    if "-f" not in data:
        file_data = "file.txt"
    else:
        file_data = data[-1]

    return directory_data, file_data


def get_path(*args: str | list) -> str:
    """
    Function for collecting path
    """
    return os.path.join(*args)


def create_path(data: list[str]) -> str:
    """
    Function to get the full destination path. If there were no directories in
    the terminal data, it will return a string with only the file name.
    """
    directory_path, file_name = get_directory_and_file(data)

    if not directory_path:
        full_path = file_name
    else:
        path = get_path(*directory_path)
        os.makedirs(path, exist_ok=True)
        full_path = get_path(path, file_name)

    return full_path


def write_to_file(path: str, mode: str) -> None:
    """
    Function for writing to a file. Gets a string and a mod
    for correct operation
    """
    current_time = datetime.datetime.now()

    with open(path, mode) as destination_file:
        destination_file.write(current_time.strftime("%Y-%m-%d %X\n"))
        line_number = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                destination_file.write("\n")
                break

            destination_file.write(f"{line_number} {user_input}\n")
            line_number += 1


def main() -> None:
    data_from_terminal = sys.argv
    full_path = create_path(data_from_terminal)

    if os.path.exists(full_path):
        write_to_file(full_path, "a")
    else:
        write_to_file(full_path, "w")


if __name__ == "__main__":
    main()
