import sys
import os
import datetime


def create_file(something: list[str]) -> None:
    dir_string = f"{os.getcwd()}\\"
    date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if "-d" in something:
        for i in range(something.index("-d") + 1,
                       something.index("-f")):
            dir_string = os.path.join(dir_string, something[i])
            os.makedirs(dir_string)

    if "-f" in something:
        file_path = os.path.join(dir_string,
                                 something[something.index("-f") + 1])
        with open(file_path, "w") as f:
            flag = ""
            f.write(date + "\n")
            while True:
                flag = input("Enter content line (type 'stop' to finish): ")
                if flag == "stop":
                    break
                f.write(flag + "\n")


create_file(sys.argv)
