import os
import sys
from datetime import datetime

is_f_flag = "-f" in sys.argv
is_d_flag = "-d" in sys.argv

if is_d_flag:
    d_index = sys.argv.index("-d")
    if is_f_flag:
        f_index = sys.argv.index("-f")
        if d_index < f_index:
            directory_names = sys.argv[d_index + 1:f_index]
            file_name = sys.argv[f_index + 1]
        else:
            directory_names = sys.argv[d_index + 1:]
            file_name = sys.argv[f_index + 1]
        path = os.path.join(*directory_names)
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, file_name)
    else:
        directory_names = sys.argv[d_index + 1:]
        path = os.path.join(*directory_names)
        os.makedirs(path, exist_ok=True)
elif is_f_flag:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    full_path = file_name

if is_f_flag:
    needs_blank_line = os.path.exists(full_path)
    with open(full_path, "a") as f:
        line_order_num = 1
        if needs_blank_line:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{line_order_num} {user_input}\n")
            line_order_num += 1
