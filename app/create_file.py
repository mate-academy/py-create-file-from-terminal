import sys
import os
from datetime import datetime


def create_file() -> None:
    list_of_args = sys.argv[1:]

    def create_dir(args: list, have_a_file: bool = False) -> str:
        index_d = list_of_args.index("-d") + 1
        index_f = list_of_args.index("-f") if have_a_file else None

        list_of_dir = list_of_args[index_d:index_f]

        path_of_new_dirs = "/".join(list_of_dir)

        os.makedirs(path_of_new_dirs)

        if index_f is not None:
            return path_of_new_dirs

    def create_new_file(args: list, path: str = "") -> None:
        index_f = args.index("-f") + 1
        name_of_file = list_of_args[index_f]
        path_of_file = f"{path}/{name_of_file}" if path != "" else name_of_file

        with open(path_of_file, "w") as new_file:
            content_of_file = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_file.write(f"{content_of_file}\n")

        while True:
            answer_of_question = input("Enter content line: ")

            if answer_of_question == "stop":
                break

            with open(path_of_file, "a") as file:
                file.write(f"{answer_of_question}\n")

    if "-d" in list_of_args and "-f" not in list_of_args:
        create_dir(list_of_args, False)

    if "-f" in list_of_args and "-d" not in list_of_args:
        create_new_file(list_of_args)

    if "-d" in list_of_args and "-f" in list_of_args:
        path_to_file = create_dir(list_of_args, True)
        create_new_file(list_of_args, path_to_file)


if __name__ == "__main__":
    create_file()
