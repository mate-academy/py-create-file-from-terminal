import sys
import os
import datetime

current = datetime.datetime.now()
args = sys.argv[1:]

parent_dir = os.getcwd()

if "-d" in args:
    d_index = args.index("-d")
    dir_parts = []
    for i in range(d_index + 1, len(args)):
        if args[i].startswith("-"):
            break
        dir_parts.append(args[i])
    parent_dir = os.path.join(parent_dir, *dir_parts)
    os.makedirs(parent_dir, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args) and not args[f_index + 1].startswith("-"):
        file_name = args[f_index + 1]
        file_path = os.path.join(parent_dir, file_name)

        if os.path.exists(file_path):
            mode = "a"
        else:
            mode = "w"

        with open(file_path, mode) as f:
            f.write(current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            if mode == "a":
                f.write("\n")

            line_number = 1
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                f.write(f"{line_number} {text}\n")
                line_number += 1
    else:
        print("Ошибка: после флага -f необходимо указать имя файла.")
elif "-d" not in args:
    print("Ошибка: укажите хотя бы один флаг -d или -f.")
