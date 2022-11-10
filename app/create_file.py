import sys
import os
import datetime


def create_file():
    current_time = datetime.datetime.now()
    if sys.argv[1] == "-f":
        with open(f"{sys.argv[2]}", "a") as file:
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

            id_ = 0
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    file.write("\n")
                    break

                file.write(f"{id_} {content}\n")

                id_ += 1

    if sys.argv[1] == "-d":
        path = "/".join(sys.argv[2:])
        os.makedirs(path)


if __name__ == '__main__':
    create_file()
