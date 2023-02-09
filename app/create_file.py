import sys
import datetime
import os


amount_of_argv = len(sys.argv)
name_dir = sys.path[0]
if sys.argv[1] == "-d":
    for item in range(2, amount_of_argv):
        if sys.argv[item] == "-f":
            break
        name_dir = name_dir + "/" + str(sys.argv[item])
        os.mkdir(name_dir)

for i in range(1, amount_of_argv):
    if sys.argv[i] == "-f":
        now = datetime.datetime.now()
        with open(f"{name_dir}/{str(sys.argv[i + 1])}", "w") as f:
            f.write(f"{now.date()} {now.hour}:{now.minute}:{now.second}\n")
            for line in sys.stdin:
                if "stop" == line.rstrip():
                    break
                print(f"Enter content line: {line}")
                f.write(line)
