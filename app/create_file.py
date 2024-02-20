from datetime import datetime
import os.path
import sys


def parse_args(arguments: list, param: str) -> tuple[str | bytes, list]:
    result = ""
    if param in arguments:
        cursor = arguments.index(param)
        arguments.pop(cursor)
        if param == "-f":
            result = arguments.pop(cursor)
        else:
            result = os.path.join(*arguments[cursor:])
    return result, arguments


def handler_file(file_path: str, file_name: str) -> None:
    full_file_path = os.path.join(file_path, file_name)
    if file_path:
        os.makedirs(file_path, exist_ok=True)
    if file_name:
        with open(full_file_path, "a") as file:
            lines = []
            line_number = 1
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                lines.append(f"{line_number} {text}")
                line_number += 1
            if os.path.getsize(full_file_path) > 0:
                file.write("\n\n")
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_datetime}\n")
            file.write("\n".join(lines))


if __name__ == "__main__":
    args = sys.argv[1:]
    filename, args = parse_args(args, "-f")
    filepath, args = parse_args(args, "-d")
    handler_file(filepath, filename)
