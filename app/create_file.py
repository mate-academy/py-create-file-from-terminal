import os
import sys
from datetime import datetime


directories = []
filename = None

if "-d" in sys.argv and "-f" in sys.argv:
    if sys.argv.index("-f") > sys.argv.index("-d"):
        start = sys.argv.index("-d") + 1
        end = sys.argv.index("-f")
        directories = sys.argv[start:end]
        filename = sys.argv[end + 1]
    else:
        start = sys.argv.index("-d") + 1
        directories = sys.argv[start:]
        filename = sys.argv[sys.argv.index("-f") + 1]
elif "-d" in sys.argv:
    start = sys.argv.index("-d") + 1
    directories = sys.argv[start:]
elif "-f" in sys.argv:
    filename = sys.argv[sys.argv.index("-f") + 1]

if directories:
    os.makedirs(os.path.join(*directories), exist_ok=True)
if filename:
    file_path = os.path.join(*directories, filename)
    user_input_info = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        user_input_info.append(user_input)

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_existing_file = os.path.isfile(file_path)
    with open(file_path, "a") as file:
        if is_existing_file:
            file.write("\n")
        file.write(f"{current_datetime}\n")
        for index, line in enumerate(user_input_info, start=1):
            file.write(f"{index} {line}\n")
