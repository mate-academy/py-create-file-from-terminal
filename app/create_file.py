from datetime import datetime as dt
import sys
import os


args = sys.argv[1:]
print(args)

full_path = os.getcwd()

if "-d" in args:
    # get folders names
    d_index = args.index("-d")

    path_parts = []
    for i in range(d_index + 1, len(args)):
        if args[i].startswith("-"):
            break
        path_parts.append(args[i])
    full_path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(full_path, exist_ok=True)

if "-f" in args:
    # file name
    f_index = args.index("-f")

    file_name = args[f_index + 1]

    write_stream = open(os.path.join(full_path, file_name), "w")
    now = dt.now()
    write_stream.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    i = 1
    while True:

        line = input("Enter content line: ")

        if line == "stop":
            break

        write_stream.write(f"{i} {line}\n")
        i += 1

    write_stream.close()
