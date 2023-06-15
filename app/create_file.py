from datetime import datetime
from sys import argv
from os import makedirs, path


def create_file() -> None:
    try:
        new_file_name = argv.pop(argv.index("-f") + 1)

        argv.pop(argv.index("-f"))
    except (IndexError, ValueError):
        new_file_name = "new_file.txt"

    try:
        path_new_file = path.join(
            *argv[argv.index("-d") + 1:]
        )
    except (IndexError, ValueError, TypeError):
        path_new_file = ""
    else:
        makedirs(path_new_file, exist_ok=True)

    path_new_file = path.join(path_new_file, new_file_name)
    line_count = 0
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = (
        f"\n{timestamp}\n" if path.exists(path_new_file)
        else f"{timestamp}\n"
    )

    while True:
        user_input = input("Enter content line: ")

        if user_input == "stop":
            break

        line_count += 1
        content += f"{line_count} {user_input}\n"

    with open(path_new_file, "a") as new_file:
        new_file.write(content)


if __name__ == "__main__":
    create_file()
