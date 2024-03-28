import sys
import os
import datetime


def write_info(file_name: str) -> None:

    line = input("Enter content line: ")
    with open(file_name, "a") as file_open:
        if os.stat(file_name).st_size:
            file_open.write("\n")

        counts = 1
        while line != "stop":
            if counts == 1:
                file_open.write(datetime.datetime.now()
                                .strftime("%Y-%m-%d %H:%M:%S")
                                + "\n")
            file_open.write(f"{counts} {line}\n")
            line = input("Enter content line: ")
            counts += 1


new_path = os.path.dirname(os.path.abspath(__file__))
current_messege = sys.argv

for flag in ["-f", "-d"]:
    try:
        flag_position = current_messege.index(flag)
    except ValueError:
        if flag == "-f":
            quit("I don't have file to write, so bay.")
    else:
        next_messege = current_messege[flag_position + 1]
        if flag == "-f":
            new_file_name = next_messege
        else:
            while (flag_position < len(current_messege) - 1
                   and next_messege != "-f"):
                new_path = os.path.join(new_path,
                                        next_messege)
                os.makedirs(new_path, exist_ok=True)
                flag_position += 1


try:
    _ = open(os.path.join(new_path, new_file_name), "x")
except IOError:
    pass
write_info(os.path.join(new_path, new_file_name))
