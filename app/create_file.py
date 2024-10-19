import os
import sys
import datetime

print(sys.argv)

command = sys.argv

if "-d" in command:
    dirs = command[command.index("-d") + 1: command.index("-f")] \
        if "-f" in command else command[command.index("-d") + 1:]
    path_dirs = os.path.join(*dirs)
    os.makedirs(path_dirs, exist_ok=True)

else:
    path_dirs = ""

if "-f" in command:
    file_path = os.path.join(path_dirs, command[command.index("-f") + 1])
    with open(file_path, "a+") as file:
        current_time = datetime.datetime.now()
        file.write(str(current_time.strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        for num_of_row, file_text in enumerate(iter(input, "stop"), start=1):
            file.write(f"{num_of_row} {file_text}\n")
