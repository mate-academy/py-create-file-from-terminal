from datetime import datetime
import sys
import os

command = sys.argv
join_folders = ""

if "-d" in command and len(sys.argv) > 2:
    folders = command[2:]
    join_folders += "/".join(folders[0:2])

    if not os.path.exists(folders[0]):
        os.mkdir(folders[0])
        os.makedirs(os.path.join(folders[0], folders[1]))

if "-f" in command and len(sys.argv) > 2:
    line_number = 1
    text = ""

    while True:
        answer = input("Enter content line:")
        if answer == "stop":
            break
        text += f"{line_number} {answer}\n"
        line_number += 1

    with open(f"{os.path.join(join_folders, command[-1])}", "a") as file:
        date_time = datetime.now().strftime("%Y %m %d %H:%M:%S")
        file.write(f"{date_time}\n"
                   f"{text}")
