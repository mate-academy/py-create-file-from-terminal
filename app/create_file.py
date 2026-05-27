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
        j = dirs.index("-f")
        dirs = dirs[:j]

if "-f" in args:
    i = args.index("-f")
    file_name = args[i + 1]

# створюємо папки
path = ""

if len(dirs) > 0:
    path = "/".join(dirs)
    os.makedirs(path, exist_ok=True)

# якщо файлу нема — вихід
if file_name is None:
    print("No file name")
    exit()

file_path = path + "/" + file_name if path else file_name

# вводимо текст
lines = []

while True:
    text = input("Enter content line: ")

    if text == "stop":
        break

    lines.append(text)

# час
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = time + "\n"

i = 1
for line in lines:
    content += str(i) + " " + line + "\n"
    i += 1

# запис у файл
if os.path.exists(file_path):
    f = open(file_path, "a", encoding="utf-8")
    f.write("\n" + content)
    f.close()
else:
    f = open(file_path, "w", encoding="utf-8")
    f.write(content)
    f.close()

print("Done:", file_path)
