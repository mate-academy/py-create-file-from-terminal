import sys
import os
import datetime


from cr_dir_f import create_dir
terminal_input = ['-d', 'dir1', 'dir2']


def create_path(cr_dir=False, cr_file=False, path=os.getcwd()):
    if cr_file is False:
        folders = terminal_input[terminal_input.index("-d") + 1::]
        for folder in folders:
            path = os.path.join(path, folder)
        create_dir(path)


if __name__ == '__main__':
    create_path(cr_dir=True)


