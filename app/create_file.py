import sys
import os
import datetime


date_now = datetime.datetime.now().replace(microsecond=0)
current_path = sys.argv


def write_in_file(file_name: str) -> None:
    str_num = 1
    while True:

        if os.path.exists(f"{file_name}"):
            with open(f"{file_name}", "r+") as file:
                last_line = file.readlines()[-1]
                if last_line[-1].strip() == "":
                    file.write(f"\n{date_now}")

            text = f"\n{str_num} {input("Enter content line: ")}"
            if "stop" in text:
                with open(f"{file_name}", "a") as file:
                    file.write("\n")
                break
            with open(f"{file_name}", "a") as file:
                file.write(f"{text}")
            str_num += 1
        else:
            with open(f"{file_name}", "w") as file:
                file.write(f"{date_now}")


if "-d" in current_path and "-f" in current_path:
    file_path = os.path.join(current_path[2], current_path[3], current_path[5])
    parent_path = os.path.dirname(file_path)
    if not os.path.exists(parent_path):
        os.makedirs(os.path.join(current_path[2], current_path[3]))
        write_in_file(file_path)
    else:
        write_in_file(file_path)

if "-d" in current_path and "-f" not in current_path[4]:
    os.makedirs(os.path.join(current_path[2], current_path[3]))

if "-f" in current_path and "-d" not in current_path[1]:
    write_in_file(current_path[2])
