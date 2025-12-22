import os
import sys
import datetime

args = sys.argv
for i in range(len(args)):
    if args[i] == "-d":
        print(f"creating directories {args[i + 1]}, {args[i + 2]}")
        os.mkdir(args[i + 1])
        os.mkdir(args[i + 2])
    elif args[i] == "-f":
        print(f"creating file {args[i + 1]}")
        with open(args[i + 1], "a") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    + "\n")
            while True:
                line = input("Enter content line:")
                if line.lower() == "stop":
                    f.write("\n")
                    break
                f.write(line + "\n")
