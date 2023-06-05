import argparse
#
import sys  # argv
import os  # makedirs
import datetime  # .strftime()

print("start")
ARGS = ""

dir_path = ""  # from term -d all items = path
file_name = ""  # from term -f first item = file name
file_content = ""  # from term
flag = ""  # -d -f


def argument_parser():
    print("parsefunc start")
    parser = argparse.ArgumentParser()
    print("SYS.ARGV: ", sys.argv)
    print("argparse.ArgumentParser(): ", parser)




if __name__ == '__main__':
    argument_parser()
# python create_file.py -d dir1 dir2 #- creates directory dir1/dir2 inside current directory.