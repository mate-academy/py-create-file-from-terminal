import sys
import os
import datetime


def create_directory(path: str) -> None:
    # Create a directory (including parent directories if needed)
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")


def create_file(file_path: str) -> None:
    # Create a file and allow user to input content
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            line_number = 1
            while True:
                content_line = input("Enter content line: ")
                if content_line == "stop":
                    break
                file.write(f"{line_number} {content_line}\n")
                line_number += 1
            print(f"File '{file_path}' created with content.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py -d "
              "<directory_path> or -f <file_name>")
        return

    flag = sys.argv[1]

    if flag == "-d":
        # Create directories if flag -d is passed
        if len(sys.argv) < 3:
            print("Error: Directory path is required after -d flag.")
            return
        directory_path = os.path.join(os.getcwd(), *sys.argv[2:])
        create_directory(directory_path)

    elif flag == "-f":
        # Create a file if flag -f is passed
        if len(sys.argv) < 3:
            print("Error: File name is required after -f flag.")
            return
        file_name = sys.argv[2]
        file_path = os.path.join(os.getcwd(), file_name)
        create_file(file_path)

    elif flag == "-d" and "-f" in sys.argv:
        # Create both directory and file if both flags are used
        if len(sys.argv) < 4:
            print("Error: Both directory path and file name are required.")
            return
        directory_path = os.path.join(os.getcwd(), *sys.argv[2:-2])
        file_name = sys.argv[-2]
        file_path = os.path.join(directory_path, file_name)
        create_directory(directory_path)
        create_file(file_path)

    else:
        print("Invalid arguments. Use -d for directory or -f for file.")


if __name__ == "__main__":
    main()
