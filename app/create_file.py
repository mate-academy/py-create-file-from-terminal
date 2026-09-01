import sys
import os
from datetime import datetime


def create_app(path: str, file_name: str, file_content: str) -> None:
    full_path = os.path.join(path, file_name)
    print(full_path)
    os.makedirs(path, exist_ok=True)
    with open(full_path, "a") as f:
        f.write(file_content)


try:
    d_idx = sys.argv.index("-d")
except ValueError:
    d_idx = -1
try:
    f_idx = sys.argv.index("-f")
except ValueError:
    f_idx = -1
if f_idx != -1:
    file_name = sys.argv[f_idx + 1]
else:
    file_name = None
if d_idx != -1:
    if f_idx != -1 and d_idx < f_idx:
        dir_path = sys.argv[d_idx + 1: f_idx]
    else:
        dir_path = sys.argv[d_idx + 1:]
    path = os.path.join(*dir_path)
else:
    path = "."
if file_name is None:
    os.makedirs(path, exist_ok=True)
else:
    content = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        content.append(user_input)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = timestamp + "\n"
    for i, line in enumerate(content, 1):
        formatted += f"{i} {line}\n"
    full_path = os.path.join(path, file_name)
    if os.path.exists(full_path):
        formatted = "\n" + formatted

    create_app(path, file_name, formatted)
