import sys
import os
import datetime


def create_dir(directories: list) -> None:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        datatime_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{datatime_line}\n")
        string_index = 1
        while True:
            content = input("Enter content line or 'stop' to finish: ")
            if content == "stop":
                break
            new_file.write(f"{string_index} Line{string_index} {content}\n")
            string_index += 1


def main() -> None:
    path = sys.argv[1:]

    if "-d" in path and "-f" in path:
        d_index = path.index("-d")
        f_index = path.index("-f")

        create_dir(path[d_index + 1:f_index])
        path[f_index], path[f_index + 1] = path[f_index + 1], path[f_index]
        path_to_file = os.path.join(*path[d_index + 1:f_index + 1])
        create_file(path_to_file)

    elif "-d" in path:
        d_index = path.index("-d")
        create_dir(path[d_index + 1:])

    elif "-f" in path:
        f_index = path.index("-f")
        create_file(path[f_index + 1])


if __name__ == "__main__":
    main()
