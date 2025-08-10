import os
import sys
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

args = sys.argv
index_f = 0
path = ""
try:
    index_d = args.index("-d")
    for i in range(index_d + 1, len(args)):
        if args[i] == "-f":
            index_f = i
            break
        path += args[i] + "/"
        if not os.path.exists(path):
            os.makedirs(path)
except ValueError:
    pass

try:
    index_f = args.index("-f")
    name_file = path + args[index_f + 1]
    exist = 0
    if os.path.exists(name_file):
        exist = 1
    with open(name_file, "a") as f:
        if exist == 1:
            f.write("\n")

        number_str = 0
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(formatted_time + "\n")

        while True:
            number_str += 1
            text = input("Enter content line:")
            if text == "stop":
                break
            f.write(str(number_str) + " " + text + "\n")

except ValueError:
    pass
