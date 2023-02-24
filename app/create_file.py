import datetime
import os
import sys


def create_file(file_name: str) -> None:
    with open(file_name, "a") as writer:
        count = 1
        while (line := input("Enter content line: ")) != "stop":
            if count == 1:
                if os.stat(file_name).st_size != 0:
                    writer.write("\n\n")
                writer.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            writer.write(f"\n{count} {line}")
            count += 1


def main() -> None:
    file_path = []
    flag = None
    for arg in sys.argv[1:]:
        if arg in ("-d", "-f"):
            flag = arg
        else:
            file_path.append(arg)

    if flag == "-f":
        if len(file_path) > 1:
            os.makedirs(os.path.join(*file_path[:-1]), exist_ok=True)
        create_file(os.path.join(*file_path))
    elif flag == "-d":
        os.makedirs(os.path.join(*file_path), exist_ok=True)


main()
