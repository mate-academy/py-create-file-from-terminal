import sys
import os
from datetime import datetime

args = sys.argv[1:]

dir_parts = []
file_name = None

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        while i < len(args) and args[i] not in ["-f", "-d"]:
            dir_parts.append(args[i])
            i += 1
    elif args[i] == "-f":
        i += 1
        if i < len(args):
            file_name = args[i]
            i += 1
    else:
        i += 1

dir_path = ""
if dir_parts:
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)

file_path = file_name
if dir_path and file_name:
    file_path = os.path.join(dir_path, file_name)

if not file_name:
    print("Diretório criado:", dir_path)
    sys.exit()

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_exists_and_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0

with open(file_path, "a", encoding="utf-8") as f:
    if file_exists_and_not_empty:
        f.write("\n")
    f.write(timestamp + "\n")
    for idx, content in enumerate(lines, start=1):
        f.write(f"{idx} {content}\n")
        
print("Arquivo criado/atualizado com sucesso", file_path)
