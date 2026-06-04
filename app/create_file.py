import sys
import os
from datetime import datetime


list_for_parsing = sys.argv


def create_dirrectory(way_file_arg: str) -> None:
    if way_file_arg is None:
        return

    if not os.path.exists(way_file_arg):
        os.makedirs(way_file_arg)


def writing_and_create_the_file(file_name_arg: str) -> None:
    if file_name_arg is None:
        return

    dop = ""
    list_to_writing = []
    if os.path.exists(file_name_arg):
        dop = "\n"

    with open(file_name_arg, "a", encoding="utf-8") as file:
        file.write(f"{dop}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        while True:
            current_string = input("Enter content line: ")
            if current_string.lower() == "stop":
                break
            list_to_writing.append(current_string)
        for step, step_str in enumerate(list_to_writing, start=1):
            file.write(f"{step} {step_str}\n")


d_index = None
f_index = None

for index in range(len(list_for_parsing)):
    if list_for_parsing[index] == "-d":
        d_index = index
    if list_for_parsing[index] == "-f":
        f_index = index


list_way_file = None
way_file = None
file_name = None
full_way_and_name = None

if f_index is not None:
    file_name = list_for_parsing[f_index + 1]

if d_index is not None and f_index is not None:
    if d_index < f_index:
        list_way_file = list_for_parsing[d_index + 1: f_index]
    elif f_index < d_index:
        list_way_file = list_for_parsing[d_index + 1::]
elif d_index is not None and f_index is None:
    list_way_file = list_for_parsing[d_index + 1::]

if list_way_file is not None:
    way_file = os.path.join(*list_way_file)
    if file_name is not None:
        list_way_file.append(file_name)
        full_way_and_name = os.path.join(*list_way_file)

if f_index is None:
    create_dirrectory(way_file)
elif d_index is None:
    writing_and_create_the_file(file_name)
else:
    create_dirrectory(way_file)
    writing_and_create_the_file(full_way_and_name)
