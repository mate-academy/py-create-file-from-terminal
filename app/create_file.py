import sys
import os
from datetime import datetime

from error import NotEnoughArguments, InvalidFlagError


def create_file(file_path: str) -> None:
    """Creates a file and timestamp."""
    with open(file_path, "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{time}\n")
        line_number = 1

        while True:
            content = input(f"Enter content line ({line_number}): ")
            if content.strip().lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1
    print(f"File '{file_path}' created successfully.")


def create_directory(directory_path: str) -> None:
    """Creates a directory."""
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        raise NotEnoughArguments(
            "No arguments were provided.Please provide the required arguments."
        )

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        directory_path = os.path.join(*args[d_index + 1:f_index])
        create_directory(directory_path)

        file_name = args[f_index + 1]
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)

    elif "-d" in args:
        d_index = args.index("-d")
        directory_path = os.path.join(*args[d_index + 1:])
        create_directory(directory_path)

    elif "-f" in args:
        f_index = args.index("-f")
        if len(args) <= f_index + 1:
            raise NotEnoughArguments(
                "No file name provided after the '-f' flag."
            )
        file_name = args[f_index + 1]
        create_file(file_name)
    else:
        raise InvalidFlagError(
            "Invalid flag. Use '-d' for directory or '-f' for file."
        )


if __name__ == "__main__":
    try:
        main()
    except (NotEnoughArguments, InvalidFlagError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
