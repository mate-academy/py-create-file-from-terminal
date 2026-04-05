import os
import sys
from datetime import datetime

args = sys.argv[1:]
file_name = None
dirs = []

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        if i < len(args):
            file_name = args[i]
            i += 1
        else:
            print("Error: File name not provided after -d.")
            sys.exit(1)
    else:
        i += 1

if not file_name:
    print("Error: File name not provided. Use -d <filename>")
    sys.exit(1)

directory_path = os.path.join(*dirs) if dirs else ""
if directory_path:
    os.makedirs(directory_path, exist_ok=True)

print(f"Target file: {file_name}")
print("Enter content lines (type 'stop' to finish):")
lines = []

while True:
    try:
        line = input("> ").strip()
        if line.lower() == "stop":
            break
        if line:
            lines.append(line)
    except EOFError:
        break

if not lines:
    print("No content entered. Exiting.")
    sys.exit(0)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
numbered_lines = [f"{idx} {text}" for idx, text in enumerate(lines, start=1)]
block = timestamp + "\n" + "\n".join(numbered_lines) + "\n"

full_path = os.path.join(directory_path, file_name)\
    if directory_path else file_name
file_exists = os.path.exists(full_path)

mode = "a" if file_exists else "w"

try:
    with open(full_path, mode, encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(block)
    print(f"Successfully written to {full_path}")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
