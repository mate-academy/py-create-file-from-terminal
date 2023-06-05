import argparse
#
import sys  # argv
import os  # makedirs
import datetime  # .strftime()

print("start")
ARGS = ""
terminal_input = sys.argv[1::]
dir_path = ""  # from term -d all items = path
file_name = ""  # from term -f first item = file name
file_content = ""  # from term
flag = ""  # -d -f

print(terminal_input)


def argument_parser() -> None:
    if len(terminal_input) <= 1:
        print("exit code")
        return
    print("parsefunc start")
    print("SYS.ARGV: ", sys.argv)

    # parser = argparse.ArgumentParser()
    # print("argparse.ArgumentParser(): ", parser, argparse)


if __name__ == "__main__":
    argument_parser()
# python create_file.py -d dir1 dir2 #- creates directory dir1/dir2 inside current directory.
