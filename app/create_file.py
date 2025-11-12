import sys
import os
import datetime


directory = "./"
if "-d" in sys.argv:
    index_need = sys.argv.index("-d") + 1
    directory += "/".join(sys.argv[index_need:])
    os.makedirs(directory)

if "-f" in sys.argv:
    index_need = sys.argv.index("-f") + 1
    with open(f"{directory}/{sys.argv[index_need]}", "a") as f:
        f.write(f"{datetime.datetime.now()}\n")
        i = 1
        while True:
            text = str(input("Enter content line: "))
            if text.lower() == "stop":
                f.write("\n")
                break
            f.write(f"{i} {text}\n")
            i += 1
