import datetime
import os
import sys


def make_file(file_name: str, path_to_file: str = " ") -> None:
    if path_to_file == " ":
        file_to_write = open(file_name, "a")
    else:
        file_to_write = open(f"{path_to_file}/{file_name}", "a")

    file_to_write.write(datetime.datetime.now()
                        .strftime("%Y-%m-%d %H:%M:%S") + "\n")
    i = 1

    for line in sys.stdin:
        if "stop" == line.rstrip():
            break
        file_to_write.write(f"{i} {line}")
        i += 1
        print(f"Enter content line: {line}")

    print("Enter content line: stop")


def make_directories(directories: list) -> str:
    path_directories = os.path.join(*directories)
    os.makedirs(path_directories, exist_ok=True)
    return str(path_directories)


command = sys.argv

if command[1] == "-d" and command[-2] == "-f":
    path_to_make_file = make_directories(sys.argv[2:-2])
    make_file(sys.argv[-1], path_to_make_file)
elif command[1] == "-d":
    make_directories(sys.argv[2:])
elif command[1] == "-f":
    make_file(sys.argv[2])
