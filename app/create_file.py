from datetime import datetime
import os
import sys


directory = False
write_file = False
folders = []
for arg in sys.argv[1:]:
    if arg == "-d":
        directory = True
        write_file = False
        continue
    elif arg == "-f":
        directory = False
        write_file = True
        continue
    if directory:
        folders.append(arg)
        object_path = os.path.join(*folders)
        os.mkdir(object_path)
    elif write_file:
        object_path = os.path.join(*folders, arg)
        with open(object_path, "a") as my_file:
            my_file.write(str(datetime.now()) + "\n")
            command = ""
            while True:
                command = input("Enter content line: ")
                if command == "stop":
                    break
                my_file.write(command + "\n")
