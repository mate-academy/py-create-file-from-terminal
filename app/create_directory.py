import sys
import os


def create_directory() -> tuple:
    """Function parse terminal input, creates directory
     and  return file name"""

    input_list = sys.argv
    file_name = None

    if "-d" in input_list:
        if "-f" in input_list:
            path = os.path.join(
                *input_list[input_list.index("-d") + 1:input_list.index("-f")]
            )

        else:
            path = os.path.join(
                *input_list[input_list.index("-d") + 1:]
            )
        os.makedirs(path)
        os.chdir(path)

    if "-f" in input_list:
        file_name = input_list[-1]

    return file_name, os.getcwd()
