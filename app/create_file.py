import datetime
import os
import sys


def create_file() -> None:
    arguments = sys.argv[1:]
    directories = []
    filename = None
    is_reading_dirs = False

    for index, argument in enumerate(arguments):
        if argument == "-d":
            is_reading_dirs = True
            continue
        elif argument == "-f":
            is_reading_dirs = False
            if index + 1 < len(arguments):
                filename = arguments[index + 1]
            continue

        if is_reading_dirs:
            directories.append(argument)

    path = None
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
        path = os.path.join(dir_path, filename)
    else:
        path = filename

    file_content = []
    count = 1

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        file_content.append(f"{count} {user_input}")
        count += 1

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n" + "\n".join(file_content)

    mode = "a" if os.path.exists(path) else "w"

    if mode == "a":
        content = "\n\n" + content

    with open(path, mode) as file:
        file.write(content)


if __name__ == "__main__":
    create_file()
