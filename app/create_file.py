import sys
import os
import datetime


if "-f" in sys.argv:
    file_index = sys.argv.index("-f")
    file_path = sys.argv[file_index + 1]

    if "-d" in sys.argv:
        start = sys.argv.index("-d") + 1
        if sys.argv.index("-f") > sys.argv.index("-d"):
            end = sys.argv.index("-f")
            folders = sys.argv[start:end]
        else:
            folders = sys.argv[start:]
        path = os.path.join(*folders)
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, file_path)
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    numbered_lines = []
    for number, line in enumerate(lines, start=1):
        numbered_lines.append(f"{number} {line}")
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final = time_now + "\n" + "\n".join(numbered_lines)
    file_has_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a") as file_name:
        if file_has_content:
            file_name.write("\n\n" + final)
        else:
            file_name.write(final)
if "-d" in sys.argv and "-f" not in sys.argv:
    start = sys.argv.index("-d") + 1
    folders = sys.argv[start:]

    path = os.path.join(*folders)
    os.makedirs(path, exist_ok=True)
