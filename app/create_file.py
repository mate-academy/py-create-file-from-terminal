import sys
import os
import datetime


def make_directory_or_file() -> None:
    args = sys.argv

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            component_path = args[d_index + 1: f_index]
        else:
            component_path = args[d_index + 1:]
        full_dir_path = os.path.join(*component_path)
        os.makedirs(full_dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        if "-d" in args:
            file_path = os.path.join(full_dir_path, file_name)
        else:
            file_path = file_name

        with open(file_path, "a") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"
                                                     ) + "\n")

            counter = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                f.write(f"{counter} {text}\n")
                counter += 1
