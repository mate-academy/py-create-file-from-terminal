import sys
import os
import datetime


path = sys.argv
str_path = " ".join(path)
if " -d " in str_path and " -f " in str_path:
    parts_dir = str_path.split(" -d ")
    directory_part = parts_dir[1]
    if " -f " in directory_part:
        parts_file = directory_part.split(" -f ")
        directory_path = parts_file[0].replace(" ", "/")
        file_path = parts_file[1]
    else:
        directory_path = directory_part.replace(" ", "/")
        file_path = parts_dir[0].split(" -f ")[1]
    os.makedirs(directory_path)
    result_path = os.path.join(directory_path, file_path)

    exists = os.path.exists(result_path) and os.path.getsize(result_path) > 0

    with open(result_path, "a") as new_file:
        if exists:
            new_file.write("\n")
        current_datetime = datetime.datetime.now()
        new_file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        new_file.write("\n")
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            else:
                new_file.write(f"{counter} {content}\n")
                counter += 1

elif " -d " in str_path:
    list_path = str_path.split(" -d ")[1].strip()
    os.makedirs(list_path.replace(" ", "/"))
elif " -f " in str_path:
    file_path = str_path.split(" -f ")[1].strip()

    exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as new_file:
        if exists:
            new_file.write("\n")
        current_datetime = datetime.datetime.now()
        new_file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        new_file.write("\n")
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            else:
                new_file.write(f"{counter} {content}\n")
                counter += 1
