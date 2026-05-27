import sys
import os
from datetime import datetime

args = sys.argv

dirs = []
file_name = None

# шукаємо -d і -f вручну
if "-d" in args:
    i = args.index("-d")
    dirs = args[i + 1:]

    # якщо є -f, обрізаємо директорії до -f
    if "-f" in dirs:
        flag_index = dirs.index("-f")
        dirs = dirs[:flag_index]

if "-f" in args:
    i = args.index("-f")
    file_name = args[i + 1]

# створюємо папки
path = ""

if len(dirs) > 0:
    path = "/".join(dirs)
    os.makedirs(path, exist_ok=True)

# якщо файлу нема — вихід (FIX для pytest)
if file_name is None:
    print("No file name")
else:
    # створюємо папки
    path = ""

    if len(dirs) > 0:
        path = "/".join(dirs)
        os.makedirs(path, exist_ok=True)

    file_path = path + "/" + file_name if path else file_name

    lines = []

    while True:
        text = input("Enter content line: ")

        if text == "stop":
            break

        lines.append(text)

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = time + "\n"

    i = 1
    for line in lines:
        content += str(i) + " " + line + "\n"
        i += 1

    if os.path.exists(file_path):
        file_handle = open(file_path, "a", encoding="utf-8")
        file_handle.write("\n" + content)
        file_handle.close()
    else:
        file_handle = open(file_path, "w", encoding="utf-8")
        file_handle.write(content)
        file_handle.close()

    print("Done:", file_path)
