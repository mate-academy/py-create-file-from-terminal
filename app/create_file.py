import sys

import os

import datetime


# parsing parameters
input_parameters = sys.argv
dirs_rec = False
name_rec = False
dirs_parameters = []
file_name = ""
for parameter in input_parameters:
    if parameter == "-d":
        dirs_rec = True
        name_rec = False
    elif parameter == "-f":
        dirs_rec = False
        name_rec = True
    elif dirs_rec:
        if parameter == "-f":
            dirs_rec = False
            name_rec = True
        else:
            dirs_parameters.append(parameter)
    elif name_rec:
        file_name = parameter
    else:
        pass

# make directories
path = ""
if len(dirs_parameters) > 0:
    path = "/".join(dirs_parameters)
    os.makedirs(path, exist_ok=True)
    path += "/"

# create the file with a content
file_exists = os.path.exists(path + file_name)
if len(file_name) > 0:
    with open(path + file_name, "a") as file:
        # add current timestamp
        time_format = "%Y-%m-%d %H:%M:%S"
        file.write(
            ("\n" if file_exists else "")
            + str(datetime.datetime.now().strftime(time_format))
            + "\n"
        )

        # add content lines
        content = None
        row_number = 1
        while content != "stop":
            content = input("Enter content line: ")
            if content != "stop" and content is not None:
                file.write(str(row_number) + " " + content + "\n")
                row_number += 1
