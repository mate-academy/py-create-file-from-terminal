import argparse
import datetime
import os


def main() -> None:
    directories, file_name = get_args()
    create_directories(directories)

    if file_name:
        full_path = get_full_path(directories, file_name)
        with open(full_path, "a") as file:
            if os.path.getsize(full_path) != 0:
                file.write("\n\n")
            current = datetime.datetime.now()
            file.write(current.strftime("%Y-%m-%d %H:%M:%S"))
            line_num = 1
            while True:
                line = input("Enter content line: ")
                if line.strip() != "stop":
                    file.write("\n" + str(line_num) + " " + line)
                    line_num += 1
                else:
                    break


def get_args() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = vars(parser.parse_args())
    return args["d"], args["f"]


def create_directories(directories: list | None) -> None:
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)


def get_full_path(
        directories: list | None,
        file_name: str
) -> str:
    path_parts = []

    if directories:
        path_parts.extend(directories)
    path_parts.append(file_name)
    return os.path.join(*path_parts)


if __name__ == "__main__":
    main()
