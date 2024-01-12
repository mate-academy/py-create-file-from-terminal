import os
import sys
import datetime


def script() -> None:
    args = sys.argv[1:]
    file_path = ""
    file_name = ""
    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        args = args[:args.index("-f")] + args[args.index("-f") + 2:]
    if "-d" in args:
        args = args[args.index("-d") + 1:]
        path = os.path.join(*args)
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(*args, file_name)

    with open(file_path, "w") as file:
        counter = 1
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\n")
        input_text = input("Enter content line: ")
        while input_text != "stop":
            file.write(str(counter) + " " + input_text + "\n")
            input_text = input("Enter content line: ")
            counter += 1


if __name__ == "__main__":
    script()
