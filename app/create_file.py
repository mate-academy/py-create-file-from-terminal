from datetime import datetime
import os
import sys


def create_file_from_terminal() -> None:
    """
        Create a file in a specified directory from terminal input.
        If the '-d' option is provided, the file will be placed in the
        given directory. If the directory does not exist, it will be created.

        Usage:
            python script_name.py -d <directory_name> -f <file_name>
        """
    commands = sys.argv
    if len(commands) == 1:
        raise ValueError("No commands provided! Use '-d' for "
                         "directory and '-f' for file name.")
    if "-f" in commands:
        index_f = commands.index("-f")
        file_name = commands[index_f + 1:]
        if not file_name:
            raise ValueError("No file name provided after '-f'.")

        if "-d" in commands:
            dir_path = make_dir(commands, index_f)

            full_path = os.path.join(dir_path, file_name[0])
        else:
            full_path = file_name[0]

        write_content(full_path)

    elif "-d" in commands:
        make_dir(commands)


def make_dir(commands: list, index_f: int = None) -> str:
    """
       Create a directory if it does not exist,
       based on the command-line arguments.

       Args:
           commands (list): The list of command-line arguments.
           index_f (int): The index of the '-f' flag to determine
           where the directory name ends.

       Returns:
           str: The path to the created directory.
       """
    index_d = commands.index("-d")
    name_dir = commands[index_d + 1:index_f]
    if not name_dir:
        raise ValueError("No directory name provided after '-d'.")
    dir_path = os.path.join(*name_dir)

    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def write_content(full_path: str) -> None:
    """
       Write content into the file specified by full_path.
       Appends a timestamp and content lines entered by the user.
       Stops when the user inputs 'stop'.

       Args:
           full_path (str): The complete path
           to the file to write content to.
       """
    line_number = 1
    time_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = ""
    while True:
        line_content = input("Enter content line: ")
        if line_content == "stop":
            break
        file_content += f"{line_number} Line{line_number} {line_content}\n"
        line_number += 1

    with open(full_path, "a") as file:
        file.write(f"{time_format}\n")
        file.write(file_content)
        file.write("\n")


if __name__ == "__main__":
    create_file_from_terminal()
