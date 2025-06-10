import os
import sys
import datetime


def decode_parameters() -> tuple:
    parameters = sys.argv
    file_name = None
    directory = []
    if "-f" in parameters:
        try:
            index = parameters.index("-f") + 1
            file_name = parameters[index]
        except IndexError as e:
            print(f"File name is missing. Error: {e}")
    if "-d" in parameters:
        index = parameters.index("-d") + 1
        for i in range(index, len(parameters)):
            if parameters[i] == "-f":
                break
            directory.append(parameters[i])
    return directory, file_name


def create_file() -> None:
    directory, file_name = decode_parameters()
    print()
    if directory:
        try:
            path = os.path.join(*directory)
            os.makedirs(path)
        except FileExistsError:
            print("Such directory already exists")
        except OSError as e:
            print(f"Error creating directory: {e}")
    if file_name:
        current_date = datetime.datetime.now()
        try:
            file_name = os.path.join(*directory, file_name)
            with open(file_name, "x") as f:
                f.write(f"{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n")
                data = input("Enter content line: ")
                count = 0
                while data != "stop":
                    count += 1
                    f.write(f"{count} {data}\n")
                    data = input("Enter content line: ")
        except FileExistsError:
            print("Such file already exists")
        except OSError as e:
            print(f"Error creating directory: {e}")
