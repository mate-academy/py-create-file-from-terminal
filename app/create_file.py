import sys
import os
import datetime


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
arguments = sys.argv
directory_path = ""


def create_file(path: str) -> None:
    content_lines = []
    print("Enter content line: ")
    while True:
        line = input()
        if line == "stop":
            break
        content_lines.append(line)
    formatted_info = f"{formatted_datetime}\n" + "\n".join(
        [f"{i + 1} {line}" for i, line in enumerate(content_lines)])
    with open(path, "w") as file_to_create:
        file_to_create.write(formatted_info)


def main() -> None:
    index = 0
    global directory_path
    while index < len(arguments):
        if arguments[index] == "-d":
            directory_path = arguments[index + 1: index + 3]
            directory_path = os.path.join(directory_path[0], directory_path[1])
            os.makedirs(directory_path, exist_ok=True)
            index += 2
        elif arguments[index] == "-f":
            file_name = arguments[index + 1]
            file_path = os.path.join(directory_path, file_name)
            create_file(file_path)
            index += 2
        else:
            index += 1


if __name__ == "__main__":
    main()
