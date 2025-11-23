import os
import sys
from datetime import datetime


def collect_lines() -> list:
    """Збирає рядки контенту від користувача до 'stop' і додає нумерацію"""
    lines = []
    count = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{count} {line}")
        count += 1
    return lines


# --- обробка директорій ---
dir_parts = []
command_line = sys.argv

if "-d" in command_line:
    d_index = command_line.index("-d") + 1
    if "-f" in command_line:
        f_index = command_line.index("-f")
        dir_parts = command_line[d_index:f_index]
    else:
        dir_parts = command_line[d_index:]

dir_path = ""
if dir_parts:
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)

# --- обробка файлу ---
file_name = None
if "-f" in command_line:
    f_index = command_line.index("-f") + 1
    if f_index < len(command_line):
        file_name = command_line[f_index]
    else:
        print("Error: No file name specified after -f")
        sys.exit(1)

if file_name:
    full_path = os.path.join(dir_path, file_name) if dir_path else file_name

    # збір рядків від користувача
    lines = collect_lines()

    # timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # запис у файл (append)
    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")  # separator before new block
        output_file.write(timestamp + "\n")
        for line in lines:
            output_file.write(line + "\n")

# --- якщо нічого не передано ---
if "-d" not in command_line and "-f" not in command_line:
    print("You must pass -d or -f")
