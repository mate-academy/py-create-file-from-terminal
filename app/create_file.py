import os
import sys
import datetime


command = sys.argv
print(command)
if "-f" in command:
    file_name = command[-1]
    print(f"i find file name. {file_name}")
    if "-d" in command:
        dir_list = command[command.index("-d") + 1:command.index("-f")]
        path = os.path.dirname("/".join(dir_list) + "/")
        os.makedirs(path, exist_ok=True)
        file_name = f"{path}/{file_name}"
    print(file_name)
    with open(file_name, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        input_command = ""
        lines = 0
        while input_command != "stop":
            input_command = input("Enter content line: ")
            if input_command == "stop":
                file.write(f"\n")
                break
            lines += 1
            file.write(f"{lines} {input_command}\n")
elif "-d" in command:
    path = os.path.dirname("/".join(command[command.index("-d") + 1:]) + "/")
    os.makedirs(path, exist_ok=True)
