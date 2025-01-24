import sys
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:

    current_dir = os.getcwd()

    full_path = os.path.join(current_dir, directory_path)

    os.makedirs(full_path, exist_ok=True)
    print(f"Directory structure '{full_path}' created.")


def create_file(name: str) -> None:
    # Ensure the directories exist before creating the file
    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        create_directory(directory)

    if os.path.exists(name):
        # Open the file in append mode if it already exists
        text_file = open(name, "a")
        current_time = datetime.now()
        formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        text_file.write(formatted_timestamp + "\n")
        while True:
            temp = input("Enter new line of content: ")
            if temp == "stop":
                text_file.close()
                break
            text_file.write(temp + "\n")
        return

    # Create a new file if it does not exist
    text_file = open(name, "w")
    current_time = datetime.now()
    formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    text_file.write(formatted_timestamp + "\n")
    while True:
        temp = input("Enter new line of content: ")
        if temp == "stop":
            text_file.close()
            break
        text_file.write(temp + "\n")


def main() -> None:
    args = sys.argv[1:]
    if args[0] == "-d":
        args.pop(0)
        result_str = "/".join(args)
        create_directory(result_str)
        return
    elif args[0] == "-f":
        create_file(args[1])
        return


main()
