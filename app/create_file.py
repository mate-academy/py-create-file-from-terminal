import os
import datetime
import argparse


def create_directories(path: list[str], directory_list: list[str]) -> None:
    if directory_list:
        for name_directory in directory_list:
            path[0] = os.path.join(path[0], name_directory)
            os.makedirs(path[0], exist_ok=True)


def create_file(path: list[str], name_of_file: str) -> None:
    time_now = datetime.datetime.now()

    if name_of_file:
        with open(os.path.join(path[0], name_of_file), "a") as file_in:
            file_in.writelines(f"{time_now.strftime('%Y-%m-%d %X')}\n")
            count = 1

            while True:
                user_input = input("content line: ")
                if user_input == "stop":
                    return file_in.writelines("\n")
                file_in.writelines(f"{count} {user_input}\n")
                count += 1


if __name__ == "__main__":
    parses = argparse.ArgumentParser()

    parses.add_argument("-d", "--directory", dest="directory", nargs="*")
    parses.add_argument("-f", dest="file_name", action="append")
    args = parses.parse_args()

    final_path = [os.getcwd()]

    directory = args.directory
    file_name = args.file_name

    create_directories(path=final_path, directory_list=directory)
    create_file(path=final_path, name_of_file=file_name[0])
