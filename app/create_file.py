import sys
from datetime import datetime
import os

if len(sys.argv) < 2:
    print("Помилка: потрібно вказати флаг -f або -d")
    sys.exit(1)

mode = None
directory = []
filename = None

for arg in sys.argv[1:]:
    if arg == "-d":
        mode = "dirs"
        continue
    if arg == "-f":
        mode = "file"
        continue
    if mode == "dirs":
        directory.append(arg)
    elif mode == "file":
        if filename is None:
            filename = arg
        else:
            print(f"Ігнорую зайвий аргумент для файлу: {arg}")
if directory:
    path = os.path.join(*directory)
    os.makedirs(path, exist_ok=True)
else:
    path = ""

if filename:
    full_file_path = os.path.join(path, filename)
    now = datetime.now()
    if os.path.exists(full_file_path):
        file_mode = "a"
    else:
        file_mode = "w"

    with open(full_file_path, file_mode) as output_file:
        if file_mode == 'a':
            output_file.write("\n")
        output_file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            output_file.write(f"{counter} {text}\n")
            counter += 1
