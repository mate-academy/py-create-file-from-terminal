import os
import argparse


def create_directory(dir_path: str) -> None:
    """
    Create a directory if it does not already exist.

    Args:
        dir_path (str): Path to the directory to be created.
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory '{dir_path}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir_path}': {e}")


def create_file(file_path: str) -> None:
    """
    Create a file and allow the user to write content into it.

    Args:
        file_path (str): Path to the file to be created.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            print(
                f"File '{file_path}' created. "
                f"Enter content (type 'stop' to finish): "
            )
            while True:
                line = input()
                if line.lower() == "stop":
                    break
                file.write(line + "\n")
        print(f"File '{file_path}' written successfully.")
    except Exception as e:
        print(f"Error creating file '{file_path}': {e}")


def main() -> None:
    """
    Main function to handle \
    command-line arguments and create files or directories.
    """
    parser = argparse.ArgumentParser(
        description="Create files and directories."
    )
    parser.add_argument(
        "-d", "--directory", type=str,
        help="Path of the directory to create."
    )
    parser.add_argument(
        "-f", "--file", type=str,
        help="Name of the file to create."
    )

    args = parser.parse_args()

    if args.directory:
        create_directory(args.directory)

    if args.file:
        if args.directory:
            file_path = os.path.join(args.directory, args.file)
        else:
            file_path = args.file
        create_file(file_path)

    if not args.directory and not args.file:
        print(
            "No directory or file specified. "
            "Use -d for directory and -f for file."
        )


if __name__ == "__main__":
    main()
