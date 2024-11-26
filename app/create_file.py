import os
from datetime import datetime


def create_directory(path_parts: str) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []
    print("Enter content line: ", end="")
    while True:
        line = input()
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)
    existing_content = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_content = f.readlines()

    with open(file_path, "a") as f:
        if existing_content:
            f.write("\n")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    print("Welcome to the file creation program!")
    action = input("What would you like to do? "
                   "Create a directory, a file, "
                   "or both? (dir/file/both): ").strip().lower()

    if action == "dir" or action == "both":
        directory_parts = input("Enter the directory path as "
                                "space-separated parts "
                                "(e.g., 'dir1 dir2'): ").split()
        if directory_parts:
            target_path = create_directory(directory_parts)
            print(f"Directory created at: {target_path}")
        else:
            print("Error: No directory path provided.")
            return
    else:
        target_path = os.getcwd()

    if action == "file" or action == "both":
        file_name = input("Enter the file name (e.g., 'file.txt'): ").strip()
        if not file_name:
            print("Error: No file name provided.")
            return
        file_path = os.path.join(target_path, file_name)
        write_to_file(file_path)
        print(f"File created at: {file_path}")


if __name__ == "__main__":
    main()
