import sys
import os
from datetime import datetime


def parse_args(arguments: list[str]) -> dict:
    args = {"file": "", "directory": [], "flag": []}
    flag = None
    for argument in arguments:
        if argument in ["-d", "-f"]:
            flag = argument
            args["flag"].append(argument)
        elif flag == "-f":
            args["file"] = argument
        elif flag == "-d":
            args["directory"].append(argument)
    return args


def create_dir(directory_args: dict) -> str:
    if directory_args["directory"]:
        directory_path = "/".join(directory_args["directory"])
        os.makedirs(directory_path)
        return directory_path
    else:
        return ""


def create_file(file_args: dict, path: str) -> None:
    if file_args["file"]:
        file_txt: str = file_args["file"]
        if path != "":
            file_name = f"{path}/{file_txt}"
        else:
            file_name = file_txt
        date_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        input_str: str = ""
        counter: int = 0
        with open(file_name, "a") as f:
            f.write(f"{date_time}\n")
            while input_str != "stop":
                counter += 1
                input_str = input("Enter content line: ")
                if input_str != "stop":
                    f.write(f"{counter} {input_str}\n")
            f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        command_line_args = sys.argv[1:]
        parsed_args = parse_args(command_line_args)
        path_dir = create_dir(parsed_args)
        create_file(parsed_args, path_dir)
    else:
        print("Command doesn't have all arguments")
