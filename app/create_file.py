import datetime
import os
import sys


def get_params(args: list) -> dict:
    """
        Takes a list of arguments and returns
        a dictionary of parameters with corresponding values.

        Args:
            args (list):
                List of command-line arguments.

        Returns:
            dict:
                A dictionary of parameters where
                keys are flags (e.g., "-d", "-f") and
                values are corresponding parameter values.
    """

    params = {"-d": "", "-f": ""}  # Initial parameter values
    flag = None

    for arg in args:
        if arg in params:
            flag = arg
        elif flag in params:
            params[flag] = os.path.join(params[flag], arg)

    return params


def create_file() -> None:
    """
        Creates a file based on the specified parameters
        and adds content to it.

        This function reads parameters from command-line arguments,
        creates a directory if it doesn't exist, constructs the file path,
        and appends content lines with line numbers and a timestamp.

        The content lines are entered by the user
        until the input "stop" is given.
    """

    params = get_params(sys.argv)

    if not os.path.exists(params["-d"]):
        os.makedirs(params["-d"])
    file_path = f"{params['-d']}/{params['-f']}"

    with open(file_path, "a") as f:
        line_count = 0

        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time_str}\n")

        text_line = input("Enter content line: ")
        while text_line != "stop":
            line_count += 1
            f.write(f"{line_count} {text_line}\n")
            text_line = input("Enter content line: ")


if __name__ == "__main__":
    create_file()
