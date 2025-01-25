import sys
import os
import datetime


try:
    if sys.argv[1] == "-d":
        if "-f" not in sys.argv:
            path = os.path.join("/".join(sys.argv[2:]))
        else:
            index_of_f = sys.argv.index("-f")
            path = os.path.join("/".join(sys.argv[2:index_of_f]))
            os.makedirs(path, exist_ok=True)
            with open(f"{path}/{sys.argv[index_of_f + 1]}", "a") as f:
                f.write(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S\n"
                ))
                line = input("Enter content line: ")
                line = "1 " + line + "\n"
                i = 1
                while "stop" not in line:
                    f.write(line)
                    i += 1
                    line = input("Enter content line: ")
                    line = f"{i} " + line + "\n"
                f.write("\n")
        os.makedirs(path, exist_ok=True)
    elif sys.argv[1] == "-f":
        with open(sys.argv[1 + 1], "a") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = input("Enter content line: ")
            line = "1 " + line + "\n"
            i = 1
            while "stop" not in line:
                f.write(line)
                i += 1
                line = input("Enter content line: ")
                line = f"{i} " + line + "\n"
            f.write("\n")
    else:
        print("argv[1] must be either -d or -f!!!")
except IndexError:
    print(f"Not much arguments in {sys.argv}!!!")
