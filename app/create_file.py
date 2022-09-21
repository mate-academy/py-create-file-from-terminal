from datetime import datetime
import sys
import os


def create_file_from_terminal():
    # parse sys.argv for directory and file name
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        dir_list = sys.argv[d_index + 1: f_index]
    else:
        dir_list = sys.argv[d_index + 1:]
        # default file name
        file_name = "file.txt"

    # create directory
    if dir_list:
        dir_path = ""
        for i in range(len(dir_list)):
            dir_path += dir_list[i] + "/"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

    #
    with open(dir_path + file_name, "a") as file:
        # creating time stamp when file was created or opened
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # this string would be written to the file. adding time stamp here
        lines_for_write = f"{time_stamp}\n"

        # index that should be at the beginning of each line
        index = 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines_for_write += f"{index} {line}\n"
            index += 1

        file.write(lines_for_write)


create_file_from_terminal()
