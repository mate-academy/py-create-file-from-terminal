import sys
import os
import datetime


def parse_arguments() -> dict:
    parsed_args = {
        "file_name": "",
        "path": ""
    }
    arguments = sys.argv
    f_flag_index = arguments.index("-f")
    d_flag_index = arguments.index("-d")
    parsed_args["file_name"] = arguments[f_flag_index + 1]

    if d_flag_index > f_flag_index + 1:
        path_list = arguments[d_flag_index + 1:]
    else:
        path_list = arguments[d_flag_index + 1:f_flag_index]

    parsed_args["path"] = os.path.join(*path_list)
    return parsed_args


def create_file(
    file_name: str,
    path: str
) -> None:
    os.makedirs(path)
    os.chdir(path)
    with (open(file_name, "w") as file):
        creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{creation_date}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    params = parse_arguments()
    create_file(params["file_name"], params["path"])


if __name__ == "__main__":
    main()
