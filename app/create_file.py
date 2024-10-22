import datetime
import os.path
import sys


def get_directory_data(data: list[str]) -> list[str] | bool:
    """Extract directory data from the terminal arguments."""
    if "-d" not in data:
        return False
    elif "-d" in data and "-f" in data:
        return data[data.index("-d") + 1:data.index("-f")]

    return data[data.index("-d") + 1:]


def get_filename_data(data: list[str]) -> str:
    """Extract file data from the terminal arguments."""
    return data[-1] if "-f" in data else "file.txt"


def get_directory_and_file(data: list[str]) -> tuple:
    """
    We receive data from the terminal and find directories and a file
    to write to. If there are no directories, then we set the value
    to False. If there is no final file, we write a string with
    the file name.
    """
    directory_data = get_directory_data(data)
    file_data = get_filename_data(data)

    return directory_data, file_data


def create_path(data: list[str]) -> str:
    """
    Function to get the full destination path. If there were no directories in
    the terminal data, it will return a string with only the file name.
    """
    directory_path, file_name = get_directory_and_file(data)

    if not directory_path:
        return file_name

    os.makedirs(os.path.join(*directory_path), exist_ok=True)
    return os.path.join(*directory_path, file_name)


def write_to_file(path: str, mode: str) -> None:
    """
    Function for writing to a file. Gets a string and a mod
    for correct operation
    """
    current_time = datetime.datetime.now()

    with open(path, mode) as destination_file:
        destination_file.write(current_time.strftime("%Y-%m-%d %X\n"))
        line_counter = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                destination_file.write("\n")
                break

            destination_file.write(f"{line_counter} {user_input}\n")
            line_counter += 1


def main() -> None:
    terminal_arguments = sys.argv
    full_path = create_path(terminal_arguments)
    print(full_path)

    if os.path.exists(full_path):
        write_to_file(full_path, "a")
    else:
        write_to_file(full_path, "w")


if __name__ == "__main__":
    main()
