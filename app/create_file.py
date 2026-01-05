import sys
import os
import datetime


args = sys.argv[1:]
directories = []
filename = None

index_d = args.index("-d") if "-d" in args else None
index_f = args.index("-f") if "-f" in args else None

if index_d is not None:
    if index_f is not None and index_f > index_d:
        directories = args[index_d + 1:index_f]
    else:
        directories = args[index_d + 1:]


if index_f is not None:
    if index_f + 1 < len(args):
        filename = args[index_f + 1]


if "-f" in args and filename is None:
    print("Error: -f requires a filename")
    sys.exit(1)


if len(directories) != 0:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


if filename is not None:
    lines = []
    while True:
        user_text = input("Enter content line: ")
        if user_text.lower() == "stop":
            break
        lines.append(user_text)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if directories:
        file_path = os.path.join(*directories, filename)
    else:
        file_path = filename

    with open(file_path, "a") as file:
        file.write(current_time + "\n")
        for page_number, line in enumerate(lines, 1):
            file.write(f"{page_number} {line}\n")
        file.write("\n")
