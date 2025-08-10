import sys
import os
from datetime import datetime


def get_directory_path(args):
    """
    Extracts the directory path after the '-d' flag.

    Args:
        args (list): List of command-line arguments.

    Returns:
        str: The full directory path.
    """
    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index + 1 < f_index:
            return os.path.join(*args[d_index + 1:f_index])

        print("❌ Error: Directory path must be specified after '-d' and before '-f'.")
        sys.exit(1)

    print("❌ Error: Missing '-d' flag.")
    sys.exit(1)


def get_file_name(args):
    """
    Extracts the filename after the '-f' flag.

    Args:
        args (list): List of command-line arguments.

    Returns:
        str: The filename.
    """
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            return args[f_index + 1]

        print("❌ Error: A filename must be specified after '-f'.")
        sys.exit(1)

    print("❌ Error: Missing '-f' flag.")
    sys.exit(1)


def create_directory(directory_path):
    """
    Creates the specified directory if it doesn't exist.

    Args:
        directory_path (str): The path of the directory to be created.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"✅ Directory '{directory_path}' created or already exists.")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        sys.exit(1)


def write_to_file(file_path):
    """
    Writes the current timestamp and user input to the file.

    Args:
        file_path (str): The path of the file to be created and written to.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{now}\n")
            line_number = 1

            while True:
                user_input = input("Enter content line: ")
                if user_input.lower() == "stop":
                    break
                file.write(f"{line_number} {user_input}\n")
                print(f"{line_number} line: {user_input}")
                line_number += 1

        print(f"✅ File '{file_path}' successfully created and populated.")

    except Exception as e:
        print(f"❌ Error writing to file: {e}")
        sys.exit(1)


def main():
    """
    Main function to parse command-line arguments and execute
    directory creation and file writing.
    """
    user_params = sys.argv

    directory_path = get_directory_path(user_params)
    file_name = get_file_name(user_params)
    full_file_path = os.path.join(directory_path, file_name)

    create_directory(directory_path)
    write_to_file(full_file_path)


if __name__ == "__main__":
    main()
