import datetime
import os
import sys


arguments = sys.argv


if "-d" in arguments:
    d_index = arguments.index("-d") + 1
    path = "/".join(arguments[d_index:])

    if "-f" in arguments:
        f_index = arguments.index("-f")
        path = "/".join(arguments[d_index:f_index])

    os.makedirs(path, exist_ok=True)

if "-f" in arguments:
    file_name = arguments[arguments.index("-f") + 1]
    flag = "w"
    if file_name in os.listdir() or \
            ("-d" in arguments and file_name in os.listdir(path)):
        flag = "a"
        path = os.getcwd()

    elif not ("-d" in arguments):
        path = os.getcwd()

    with open(f"{path}/{file_name}", flag) as file:
        rows = [f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
        counter = 1

        while True:
            input_text = input("Enter content line: ")
            if "stop" in input_text:
                rows.append("\n")
                file.writelines(rows)
                break
            rows.append(f"{counter} {input_text}\n")
            counter += 1
