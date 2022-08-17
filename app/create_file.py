import os
import sys
from datetime import datetime

path_ = []
if "-d" in sys.argv and "-f" in sys.argv:

    path_ = [
        sys.argv[i] for i in range(2, (len(sys.argv) - 2))]
    os.makedirs("/".join(path_))
    name_file = "/".join(path_) + "/" + sys.argv[-1]

elif "-d" in sys.argv:

    path_ = [
        sys.argv[i] for i in range(2, len(sys.argv))
    ]
    os.makedirs("/".join(path_))
    name_file = "/".join(path_) + "/file.txt"

else:
    name_file = str(sys.argv[-1])

with open(name_file, "a") as f:
    f.write(str(datetime.now())[:-7] + "\n")
    print(str(datetime.now())[:-7] + "\n")
    i = 0
    print(f"Enter content line: ")
    for line in sys.stdin:
        i += 1
        if "stop" == line.rstrip():
            break
        else:
            f.write(f"{i} Line{i} {line}")
        print(f"Enter content line: Line{i} {line}")
