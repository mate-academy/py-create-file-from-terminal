import argparse
#
import sys  # argv
import os  # makedirs
import datetime  # .strftime()

ARGS = ""

dir_path = ""  # from term -d all items = path
file_name = ""  # from term -f first item = file name
file_content = ""  # from term
flag = ""  # -d -f

print("glob")


def parsefunc():
    parser = argparse.ArgumentParser()
    print(sys.argv)
    print(parser)
    print("func")


if __name__ == '__main__':
    parsefunc()
