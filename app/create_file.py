import datetime
import os
import sys


arguments = sys.argv


def file_folder_creation(args: list):
    if "-d" in args:
        d_index = args.index("-d") + 1
        path = "/".join(args[d_index:])

        if "-f" in args and args.index("-f") > args.index("-d"):
            f_index = args.index("-f")
            path = "/".join(args[d_index:f_index])

        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        flag = "w"
        if file_name in os.listdir() or \
                ("-d" in args and file_name in os.listdir(path)):
            flag = "a"
            path = os.getcwd()

        elif not ("-d" in args):
            path = os.getcwd()

        with open(f"{path}/{file_name}", flag) as file:
            rows = [
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
            counter = 1

            while True:
                input_text = input("Enter content line: ")
                if "stop" in input_text:
                    rows.append("\n")
                    file.writelines(rows)
                    break
                rows.append(f"{counter} {input_text}\n")
                counter += 1


file_folder_creation(arguments)
