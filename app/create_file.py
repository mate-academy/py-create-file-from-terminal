import os
import sys
from datetime import datetime

directory = "."
filename = "text.txt"
content = ""

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    directory = os.path.join(*sys.argv[d_index + 1:])
    os.makedirs(directory, exist_ok=True)

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]
    content = " ".join(sys.argv[f_index + 2:])

if not content:
    content_lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        content_lines.append(user_input)
        content = "\n".join(content_lines)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_path = os.path.join(directory, filename)

with open(file_path, "a") as file:
    file.write(current_time + "\n")

for index, line in enumerate(content.splitlines(), 1):
    file.write(f"{index}{line}\n")

print(f"Content has been written to {file_path}")
