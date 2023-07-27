import sys
import os
from datetime import datetime


def create_path(sys_args: list) -> dict:
    file_directory_path = {
        "directory_path": None,
        "file_path": None
    }

    if "-f" in sys_args:
        file_directory_path["file_path"] = sys_args.pop()
        sys_args.remove("-f")

    directory_names = sys_args[2:]

    if directory_names:
        directory_path = os.path.join(*directory_names)
        file_directory_path["directory_path"] = directory_path
        if file_directory_path["file_path"]:
            file_directory_path["file_path"] = os.path.join(
                directory_path, file_directory_path["file_path"]
            )

    return file_directory_path


def create_file() -> None:
    file_directory_path = create_path(sys.argv)

    if file_directory_path["directory_path"]:
        os.makedirs(file_directory_path["directory_path"], exist_ok=True)

    if file_directory_path["file_path"]:
        with open(file_directory_path["file_path"], "a") as source_file:
            source_file.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            while True:
                user_input = input("Enter content line:")
                if user_input == "stop":
                    source_file.write("\n")
                    break
                source_file.write(f"{user_input}\n")


if __name__ == "__main__":
    create_file()
