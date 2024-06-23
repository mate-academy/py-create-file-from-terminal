import sys
import datetime
import os

parent_dir = os.path.join(os.getcwd(), "app")

if "-d" == sys.argv[1]:
    for i in range(2, sys.argv.index("-f")):
        directory = sys.argv[i]
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)
        parent_dir = os.path.join(parent_dir, directory)

if "-f" in sys.argv:
    index_sys = sys.argv.index("-f")

    with open(os.path.join(parent_dir, sys.argv[index_sys + 1]), "a") as source_file:
        number_line = 0
        now = datetime.datetime.now()
        datatime_str = now.strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{datatime_str}\n")
        while True:
            number_line += 1
            new_line = input("Enter content line: ")
            if new_line.lower() == "stop":
                break
            source_file.write(f"{number_line} {new_line}\n")
