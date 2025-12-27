import sys
import os

def main():
    parse_arguments()

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
