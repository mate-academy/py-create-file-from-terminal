import os
import sys
import datetime


def script() -> None:
    args = sys.argv[1:]
    path = ""
    file_name = ""
    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        args = args[:-2]
    if "-d" in args:
        args = args[args.index("-d") + 1:]
        path = os.path.join(*args)
        os.makedirs(path, exist_ok=True)

    with open(path + "\\" + file_name, "w") as file:
        counter = 1
        file.write(datetime.strftime()(datetime.now))
        file.write()
        input_text = input("Enter content line: ")
        while input_text != "stop":
            file.write(str(counter) + " " + input_text + "\n")
            input_text = input("Enter content line: ")
            counter += 1


if __name__ == "__main__":
    script()
