import sys
from datetime import datetime
import os

if len(sys.argv) < 2:
    print("Помилка: потрібно вказати флаг -f або -d")
    sys.exit(1)

mode = None
directory = []
file = None

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
        if file is None:
            file = arg
        else:
            print(f"Ігнорую зайвий аргумент для файлу: {arg}")
if directory:
    path = os.path.join(*directory)
    os.makedirs(path, exist_ok=True)
else:
    path = ""

if file:
    full_file_path = os.path.join(path, file)
    now = datetime.now()
    if os.path.exists(full_file_path):
        file_mode = 'a'  # додаємо у кінець
    else:
        file_mode = 'w'  # новий файл

    with open(full_file_path, file_mode) as f:
        f.write(now.strftime("%m/%d/%Y %H:%M:%S") + "\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            f.write(f"{counter} {text}\n")
            counter += 1




