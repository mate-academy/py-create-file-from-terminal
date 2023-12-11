import sys
import os
import datetime

data_now = datetime.datetime.now()
current_data = data_now.strftime("%Y-%m-%d %H:%M:%S")


def write_in_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(current_data + "\n")
        length_file = 0
        while True:
            input_data = input("Enter content line: ")
            if input_data == "stop":
                break
            file.write(f"{length_file + 1} {input_data} \n")
        file.write("\n")


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        directories = sys.argv[2:-2]
        ready_path = os.path.join(*directories)
        os.makedirs(ready_path, exist_ok=True)
        path_with_name_file = os.path.join(ready_path, sys.argv[-1])
        write_in_file(path_with_name_file)

    elif "-d" in sys.argv and "-f" not in sys.argv:
        directories = sys.argv[2:]
        ready_path = os.path.join(*directories)
        os.makedirs(ready_path, exist_ok=True)

    elif "-d" not in sys.argv and "-f" in sys.argv:
        name_file = sys.argv[2:]
        write_in_file(*name_file)


if __name__ == "__main__":
    create_file()
