import os.path
import sys
import datetime


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                break
            file.write(f"{line} {line_content}\n")
            line += 1


def main() -> None:
    command_args = sys.argv[1:]

    index_d = 0
    index_f = 0
    if "-d" in command_args and "-f" in command_args:
        index_d = command_args.index("-d")
        index_f = command_args.index("-f")
        direct = command_args[index_d + 1:index_f]
        file_name = command_args[index_f + 1:]

        dir_path = str(os.path.join(*direct))
        os.makedirs(dir_path, exist_ok=True)

        file_path = str(os.path.join(*file_name))
        create_file(file_path)
    elif "-d" in command_args:
        dir_path = str(os.path.join(*command_args[index_d + 1:]))
        os.makedirs(dir_path, exist_ok=True)
    elif "-f" in command_args:
        file_path = str(os.path.join(*command_args[index_f + 1:]))
        create_file(file_path)
    else:
        print(
            "Invalid arguments. "
            "Use '-d' to create directory, "
            "or '-f' to create file"
        )
