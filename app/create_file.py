import argparse
from datetime import datetime
import os


def get_user_data() -> list[str]:
    create_time = "{} \n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user_input_data = [create_time]
    line_counter = 1
    while 1:
        user_input = input("Enter some message: ")
        if user_input.strip().lower() == "stop":
            break
        user_input_data.append(f"{line_counter} {user_input}\n")
        line_counter += 1
    return user_input_data


def write_user_data(file_name: str) -> None:
    try:
        with open(file_name, "a") as file:
            file.writelines(get_user_data())
    except IOError:
        print("Oops, something went wrong during writing data process")


def create_file(dir_path: str, file_path: str) -> None:
    if dir_path:
        path_to_dir = os.path.join(*dir_path)
        print("file directory: ", path_to_dir)
        os.makedirs(path_to_dir, exist_ok=True)
    if file_path:
        if dir_path:
            path_to_file = os.path.join(*dir_path, file_path)
            write_user_data(path_to_file)
        else:
            write_user_data(file_path)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parsed arguments including file path and directory path."
    )
    parser.add_argument(
        "-f",
        dest="file_path",
        help="Path to the file where data will be written"
    )
    parser.add_argument(
        "-d",
        nargs="+",
        dest="dir_path",
        help="Directory path where the file will be created"
    )
    return parser.parse_args()


if "__name__" == "__main__":
    args = parse_arguments()
    create_file(args.dir_path, args.file_path)
