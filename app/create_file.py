import os
import sys
from datetime import datetime


def create_dir(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except EOFError as error:
        print(f"Error: {error}")
        sys.exit(1)


def create_file(file_path: str) -> None:
    file_exist = False
    if os.path.exists(file_exist):
        file_exist = True

    with open(file_path, "a") as file:
        current_date_and_time = datetime.now()
        if file_exist:
            file.write("\n")
        file.write(f'{current_date_and_time.strftime("%y-%m-%d %H:%M:%S")}\n')

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        base_dir = os.path.join(os.getcwd(), "app")
        directory = os.path.join(base_dir, *sys.argv[dir_index:])
        create_dir(directory)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        create_file(filename)
    else:
        if "-d" in sys.argv and "-f" in sys.argv:
            dir_index = sys.argv.index("-d") + 1
            file_index = sys.argv.index("-f") + 1
            directory = os.path.join(*sys.argv[dir_index: file_index - 1])
            filename = sys.argv[file_index]
            create_dir(directory)
            file_path = os.path.join(directory, filename)
            create_file(file_path)


if __name__ == '__main__':
    main()
