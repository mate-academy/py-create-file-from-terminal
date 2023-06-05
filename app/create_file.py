import argparse
#
import sys  # argv
import os  # makedirs
import datetime  # .strftime()

print(f"{'*' * 10} START {'*' * 10}")
# terminal_input = sys.argv[::]


terminal_input = ['create_file.py', '-d', 'dir1', 'dir2', '-f', 'file.txt']

"""
1 = create dir/s
2 = create file
3 = create dir/s and file
"""


def argument_parser() -> None:
    if len(terminal_input) <= 1:
        print(f"{'*' * 10} EXIT CODE {'*' * 10}")
        return

    if "-d" in terminal_input:
        print("d here")
        condition = 1
    if "-f" in terminal_input:
        print("f here")
        condition = 2
    if "-d" in terminal_input and "-f" in terminal_input:
        print("d and f here")
        condition = 3
    print(condition)
    # next_flow(condition)

    # if "-d" in terminal_input and "-f" in terminal_input:
    #     start_path_range = terminal_input.index("-d") + 1
    #     end_path_range = terminal_input.index("-f")
    #     path = terminal_input[start_path_range:end_path_range]
    #     print("-d and -f case: ", path)
    #     create_dirs()
    #     create_file()
    #     retur

    # parser = argparse.ArgumentParser()
    # print("argparse.ArgumentParser(): ", parser, argparse)


if __name__ == "__main__":
    argument_parser()

# try:
#     for folder in terminal_input:
#         os.mkdir(os.path.join(os.getcwd(), folder))
# except FileExistsError:
#     print("Cannot create a file when that file already exists.\n"
#           "Choose another name.")
