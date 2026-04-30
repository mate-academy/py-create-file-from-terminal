import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs_create = ""


if "-d" in args:
    d_index = args.index("-d")
    f_index = args.index("-f") if "-f" in args else len(args)
    dirs = args[d_index + 1:f_index]
    if len(dirs) == 0:
        print("Error: No directories specified after -d flag")
        sys.exit(1)
    for directory in dirs:
        if directory.startswith("-"):
            print(
                f"Error: Invalid directory name '{directory}' "
                f"(starts with '-')"
            )
            sys.exit(1)
    dirs_create = os.path.join(*dirs)
    os.makedirs(dirs_create, exist_ok=True)


if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 >= len(args):
        print("Error: No filename specified after -f flag")
        sys.exit(1)
    file_name = args[f_index + 1]
    if file_name.startswith("-"):
        print(f"Error: Invalid filename '{file_name}' (starts with '-')")
        sys.exit(1)
    file_path = os.path.join(dirs_create, file_name)\
        if dirs_create \
        else file_name

    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")
        count = 1
        while True:
            try:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                f.write(f"{count} {content}\n")
                count += 1
            except EOFError:
                print("\nInput terminated.")
                break
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                sys.exit(0)
