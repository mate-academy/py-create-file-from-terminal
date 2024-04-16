import os
import sys
import datetime


def add_to_file(filename: str) -> None:
    count = 0
    with open(filename, "a") as file:
        file.write("\n" + datetime.datetime.now().
                   strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            count += 1
            terminal_line = input("Enter content line:")
            if terminal_line.lower() == "stop":
                break
            if terminal_line.strip():
                file.write(str(count) + " " + terminal_line + "\n")
            else:
                break


def create_file(filename: str) -> None:
    count = 0
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            file.write(datetime.datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S") + "\n")
            file.write(content)

    else:
        with open(filename, "a") as file:
            file.write(datetime.datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                count += 1
                terminal_line = input("Enter content line:")
                if terminal_line.lower() == "stop":
                    break
                if terminal_line.strip():
                    file.write(str(count) + " " + terminal_line + "\n")
                else:
                    break


def main() -> None:

    flag = sys.argv[1]
    if flag == "-d" and len(sys.argv) >= 3:
        directory_path = os.path.join(*sys.argv[2:])
        os.makedirs(directory_path, exist_ok=True)
    elif flag == "-f" and len(sys.argv) >= 3:
        filename = sys.argv[2]
        if os.path.exists(filename):
            add_to_file(filename)

        else:
            create_file(filename)


if __name__ == "__main__":
    main()
