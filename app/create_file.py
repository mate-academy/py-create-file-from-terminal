import sys
import os
from datetime import datetime

current_time = datetime.now()
formated_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

arg = sys.argv[1:]

d_idx = arg.index("-d") if "-d" in arg else None
f_idx = arg.index("-f") if "-f" in arg else None

directories = ""
file_path = None

# --- Obsługa -d (niezależnie od tego, czy -f występuje przed czy po -d) ---
if d_idx is not None:
    if f_idx is not None and f_idx > d_idx:
        segment = arg[d_idx + 1: f_idx]
    else:
        segment = arg[d_idx + 1:]

    for elem in segment:
        directories = os.path.join(directories, elem)

    os.makedirs(directories, exist_ok=True)

# --- Ustalenie file_path (niezależnie od tego, czy jest -d) ---
if f_idx is not None:
    filename = arg[f_idx + 1]
    file_path = os.path.join(directories, filename)

# --- Zbieranie treści od użytkownika (tylko jeśli podano -f) ---
if file_path is not None:
    lines = []
    while True:
        inp = input("Enter content line: ")
        if inp == "stop":
            break
        lines.append(inp)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as new_file:
        if file_exists:
            new_file.write("\n")
        new_file.write(formated_time + "\n")
        for line_num, line in enumerate(lines, start=1):
            new_file.write(f"{line_num} {line}\n")
