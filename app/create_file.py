import os
import sys
from datetime import datetime

command = sys.argv
current_path = os.getcwd()

if "-d" in command:
    start_index = command.index("-d") + 1
    end_index = command.index("-f") if "-f" in command else len(command)
    directories = command[start_index:end_index]
    current_path = os.path.join(current_path, *directories)
    os.makedirs(current_path, exist_ok=True)

if "-f" in command and "-f" != command[-1]:
    file_name = command[command.index("-f") + 1]
    file_name = os.path.join(current_path, file_name)
    text = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    with open(file_name, "a") as file:
        index = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            text += f"{index} {user_input}\n"
            index += 1
        file.write(text)
