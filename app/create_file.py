import sys
import os
import datetime


def create_folders(folders_names: list) -> str:
    parent_path = folders_names[0]
    os.makedirs(parent_path, exist_ok=True)
    for directory in folders_names[1:]:
        subdir_path = os.path.join(parent_path, directory)
        os.makedirs(subdir_path, exist_ok=True)
        parent_path = subdir_path
    return parent_path


def fill_in_file(file_path: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"{timestamp}\n"
    count = 1
    while True:
        user_input = input("Enter content line:")
        if user_input == "stop":
            break
        data += f"{count} {user_input}\n"
        count += 1
    with open(file_path, "a") as output:
        output.write(data)


def create_file() -> None:
    if ("-d", "-f") in sys.argv:
        dir_path = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        file_name = sys.argv[-1]
        des_path = create_folders(dir_path)
        file_path = os.path.join(des_path, file_name)
        fill_in_file(file_path)
    elif "-d" in sys.argv:
        dir_path = sys.argv[sys.argv.index("-d") + 1:]
        create_folders(dir_path)
    elif "-f" in sys.argv:
        file_name = sys.argv[-1]
        fill_in_file(file_name)


if __name__ == "__main__":
    create_file()
