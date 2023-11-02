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
    path = os.path.join(*sys_argv[2:])
    os.makedirs(path)
elif sys_argv[1] == "-f":
    if os.path.isfile(sys_argv[2]):
        create_file_for_writing(sys_argv[2], "a")
    else:
        create_file_for_writing(sys_argv[2], "w")
elif all(value in sys.argv for value in ["-d", "-f"]):
    index_f = sys_argv.index("-f")
    index_d = sys_argv.index("-d")
    if index_f > index_d:
        path = os.path.join(*sys_argv[index_d: index_f])
        os.makedirs(path)
    path = os.path.join(*sys_argv[index_f: index_d])
    os.makedirs(path)
    create_file_for_writing(sys_argv[index_f + 1], "w")
