import datetime
import os
import sys


def write_content_to_file(file_path, timestamp):
    line_number = 1
    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def create_file():
    path = ""
    filename = ""
    args = sys.argv[1:]

    if "-d" in args:
        directory_flag_index = args.index("-d")
        path = os.path.join(*args[directory_flag_index + 1:args.index("-f")] if "-f" in args else args[directory_flag_index + 1:])
        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        file_flag_index = args.index("-f")
        filename = args[file_flag_index + 1]

    file_path = os.path.join(path, filename) if path else filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path):
        write_content_to_file(file_path, timestamp)
    else:
        with open(file_path, "w") as file:
            file.write(f"{timestamp}\n")
        write_content_to_file(file_path, timestamp)

    print(f"File created at: {file_path}")


if __name__ == "__main__":
    create_file()
