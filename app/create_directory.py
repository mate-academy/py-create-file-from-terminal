import sys
import os


def create_directory() -> str:
    """Function parse terminal input, creates directory
     and  return file name"""

    input_list = sys.argv
    file_name = "file.txt"

    if "-d" in input_list and "-f" in input_list:
        path = os.path.join(
            *input_list[input_list.index("-d") + 1:input_list.index("-f")]
        )
        file_name = input_list[-1]
        os.makedirs(path)
        os.chdir(path)

    elif "-d" in input_list:
        path = os.path.join(
            *input_list[input_list.index("-d") + 1:]
        )
        os.makedirs(path)
        os.chdir(path)

    elif "-f" in input_list:
        file_name = input_list[-1]

    return file_name
