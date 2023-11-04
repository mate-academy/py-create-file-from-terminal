import datetime
import sys
import os


def create_file() -> None:
    current_time = datetime.datetime.now()
    if "-d" in sys.argv:
        for i in range(2, len(sys.argv)):
            if "-f" not in sys.argv[i]:
                os.mkdir(sys.argv[i])
                os.chdir(sys.argv[i])
            else:
                break

    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file:
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            count_lines = 1

            while True:
                user_typing = input("Enter content line:")
                if user_typing == "stop":
                    file.write("\n")
                    break
                file.write(f"{count_lines} {user_typing}" + "\n")
                count_lines += 1


create_file()
