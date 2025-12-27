import sys
import os
import datetime

def main():
    params = parse_arguments()
    create_file(params["file_name"], params["path"])

def parse_arguments():
    parsed_args = {
        "file_name": "",
        "path": ""
    }
    arguments = sys.argv
    f_index = arguments.index("-f")
    d_index = arguments.index("-d")
    parsed_args["file_name"] = arguments[f_index + 1]
    *path_list, = arguments[d_index + 1:] if d_index > f_index + 1 else arguments[d_index + 1:f_index]
    parsed_args["path"] = os.path.join(*path_list)
    return parsed_args

def create_file(
    file_name: str,
    path: str
):
    os.makedirs(path)
    os.chdir(path)
    with open(file_name, "w") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        i = 1
        content = input("Enter content line: ")
        while content != "stop":
            file.write(f"{i} {content}")

main()