import sys
import os
import datetime


folder_name = []
file_name = None
target_dir = ""
final_path = ""

idx_f = sys.argv.index("-f") if "-f" in sys.argv else None
idx_d = sys.argv.index("-d") if "-d" in sys.argv else None


if idx_f is not None:
    file_name = sys.argv[idx_f + 1]

if idx_d is not None:
    if idx_f is not None and idx_f > idx_d:
        end_idx = idx_f
    else:
        end_idx = len(sys.argv)

    folder_name = sys.argv[idx_d + 1 : end_idx]

if folder_name:
    target_dir = os.path.join("", *folder_name)
    os.makedirs(target_dir, exist_ok=True)

if file_name:
    final_path = os.path.join(target_dir, file_name)

if final_path:
    content = []
    while True:
        line = input("Enter content line:")

        if line == "stop":
            break

        content.append(line)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(final_path, "a") as file:
        file.write(now + "\n")

        for index, line in enumerate(content, start=1):
            row = file.write(f"{index} {line}\n")

        file.write("\n")
