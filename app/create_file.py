import datetime
import sys
import os


def file_creater():
    current = datetime.datetime.now()
    if "-d" in sys.argv and "-f" in sys.argv:
        for i in range(2, len(sys.argv[:-2])):
            os.mkdir(sys.argv[i])
            os.chdir(sys.argv[i])
        with open(sys.argv[-1], "a") as file:
            file.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")
            count_lines = 1

            while True:
                user_typing = input("Enter content line:")
                if user_typing == "stop":
                    file.write("\n")
                    break
                file.write(f"{count_lines} {user_typing}" + "\n")
                count_lines += 1

    elif "-d" in sys.argv:
        for i in range(2, len(sys.argv)):
            os.mkdir(sys.argv[i])
            os.chdir(sys.argv[i])

    elif "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file:
            file.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")
            count_lines = 1
            while True:
                user_typing = input("Enter content line:")
                if user_typing == "stop":
                    file.write("\n")
                    break
                file.write(f"{count_lines} {user_typing}" + "\n")
                count_lines += 1


file_creater()
