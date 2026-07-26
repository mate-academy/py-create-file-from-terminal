import sys
import os
import datetime


args = sys.argv[1:]
index_dict = {}
dir_dest = ""
file_name = ""


def write_in_file(place: str) -> None:
    with open(place, "a+") as file:
        current_time = datetime.datetime.now()
        file.write(f'{current_time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        counter = 1
        while True:
            input_text = input("Enter content line: ")
            if input_text.lower() == "stop":
                break
            file.write(f"{counter} {input_text}\n")
            counter += 1


# Знаходжу індекси входжень -d та -f
for key, value in enumerate(args):
    if value == "-d":
        index_dict[value] = key
    if value == "-f":
        index_dict[value] = key


# Роблю перевірку за умов якщо є -d і -f
if "-d" in index_dict and "-f" in index_dict:
    if args[index_dict["-d"] + 1] == "-f":
        raise Exception("NO DIR NAME GIVEN")
    if index_dict["-f"] + 1 >= len(args):
        raise Exception("NO FILE NAME GIVEN")
    dir_dest = args[index_dict["-d"] + 1:index_dict["-f"]]
    dir_dest = os.path.join(*dir_dest)
    file_name = args[index_dict["-f"] + 1]

# Роблю перевірку за умов якщо є тільки -d
elif "-d" in index_dict and "-f" not in index_dict:
    if index_dict["-d"] + 1 >= len(args):
        raise Exception("NO DIR NAME GIVEN")
    dir_dest = args[index_dict["-d"] + 1:]
    dir_dest = os.path.join(*dir_dest)

# Роблю перевірку за умов якщо є тільки -f
elif "-d" not in index_dict and "-f" in index_dict:
    if index_dict["-f"] + 1 >= len(args):
        raise Exception("NO FILE NAME GIVEN")
    file_name = args[index_dict["-f"] + 1]

# Створюю шлях
if dir_dest != "" and file_name != "":
    full_dest = os.path.join(".", dir_dest, file_name)
    os.makedirs(dir_dest, exist_ok=True)
    write_in_file(full_dest)
elif dir_dest == "" and file_name != "":
    write_in_file(file_name)
elif dir_dest != "" and file_name == "":
    os.makedirs(dir_dest, exist_ok=True)
