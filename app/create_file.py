import os

import sys

from datetime import datetime

sys_argv = sys.argv


def create_file_for_writing(
    file_name: str,
    editing_param: str
) -> None:
    with open(file_name, editing_param) as file:
        file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        data = input("Enter content line:")
        while data != "stop":
            file.write(data)
            data = input("Enter content line:")


if sys_argv[1] == "-d":
    os.makedirs("/".join(sys_argv[2:len(sys_argv) - 1]))
elif sys_argv[1] == "-f":
    if os.path.isfile(sys_argv[2]):
        create_file_for_writing(sys_argv[2], "a")
    else:
        create_file_for_writing(sys_argv[2], "w")
elif "-f" in sys.argv and "-d" in sys.argv:
    os.makedirs("/".join(sys_argv[
                         sys_argv.index("-d"):sys_argv.index("-f")
                         ]))
    create_file_for_writing(sys_argv[-1], "w")
