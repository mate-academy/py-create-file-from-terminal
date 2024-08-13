from datetime import datetime
import os
import sys


def get_user_input() -> list[str]:
    user_input = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        user_input.append(content)
    return user_input


def write_file(path: str, content_lines: list[str]) -> None:
    try:
        with open(path, "a") as file:
            now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            index = 1
            file.write(f"{now}\n")
            for content in content_lines:
                file.write(f"{index} Line {content}\n")
                index += 1
            file.write("\n")
    except Exception as e:
        print(f"An Error while writing to file: {e}")


def create_dirs(args_list: list[str]) -> str:
    file_index = args_list.index("-f")
    dirs_list = args_list[args_list.index("-d") + 1:file_index]
    dirs_path = os.path.join(*dirs_list)
    os.makedirs(dirs_path, exist_ok=True)
    file_name = args_list[file_index + 1]
    file_path = os.path.join(dirs_path, file_name)
    return file_path


def handle_args(args: list[str]) -> None:
    if "-d" in args and "-f" in args:
        write_file(path=create_dirs(args), content_lines=get_user_input())

    elif "-f" in args:
        write_file(path=args[-1], content_lines=get_user_input())

    elif "-d" in args:
        dirs_path = os.path.join(*args[args.index("-d") + 1:])
        os.makedirs(dirs_path, exist_ok=True)
    else:
        raise KeyError("Invalid arguments: You must provide "
                       "either '-d' for directory or '-f' for file, or both.")


if __name__ == "__main__":
    handle_args(sys.argv)
