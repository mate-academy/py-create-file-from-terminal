import os
import sys
from datetime import datetime


def create_directory(args: list) -> str:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(filename: str, path: str = ".") -> None:
    current = datetime.now()
    file_path = os.path.join(path, filename)
    with open(file_path, "a") as file:
        file.write(current.strftime("%Y-%m-%d %I:%M:%S") + "\n")
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                file.write("\n")
                break
            file.write(user_input + "\n")


def main() -> None:
    command = sys.argv

    if "-d" in command and "-f" in command:
        path = create_directory(command[2:-2])
        create_file(command[-1], path)
    elif "-d" in command:
        create_directory(command[2:])
    elif "-f" in command:
        create_file(command[-1])
    else:
        print("Invalid command. "
              "The command should contain '-f' or '-b' flags or both of them.")


if __name__ == "__main__":
    main()
