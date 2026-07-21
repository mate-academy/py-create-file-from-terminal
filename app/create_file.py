import sys
import os
from datetime import datetime
args = sys.argv[1:]
has_d = "-d" in args
has_f = "-f" in args
d_index = args.index("-d") if has_d else -1
f_index = args.index("-f") if has_f else -1
# Визначаємо директорію
dirs = []
if has_d:
    if has_f:
        if d_index < f_index:
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]
    else:
        dirs = args[d_index + 1:]
dir_path = os.path.join(*dirs) if dirs else ""
if dir_path:
    os.makedirs(dir_path, exist_ok=True)
# Тільки директорія - виходимо
if has_d and not has_f:
    sys.exit(0)
# Формуємо шлях до файлу
if has_f:
    file_name = args[f_index + 1]
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name
else:
    file_path = "output.txt"
# Збираємо контент
lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)
# Записуємо у файл
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "a") as f:
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        f.write("\n")
    f.write(timestamp + "\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")
