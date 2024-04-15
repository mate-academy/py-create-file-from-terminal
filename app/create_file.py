import os
import sys
import datetime


def main() -> None:

    flag = sys.argv[1]
    count = 0

    if flag == "-d" and len(sys.argv) >= 3:
        directory_path = os.path.join(*sys.argv[2:])
        print(directory_path)
        os.makedirs(directory_path, exist_ok=True)

    elif flag == "-f" and len(sys.argv) >= 3:
        filename = sys.argv[2]
        if os.path.exists(filename):
            with open(filename, "a") as file:
                file.write("\n" + datetime.datetime.now().
                           strftime("%Y-%m-%d %H:%M:%S") + "\n")
                while True:
                    count += 1
                    terminal_line = input("Enter content line:")

                    file.write(str(count) + " " + terminal_line + "\n")
                    if terminal_line.lower() == "stop":
                        break
        else:
            with open(filename, "w") as file:
                file.write("\n" + datetime.datetime.now().
                           strftime("%Y-%m-%d %H:%M:%S") + "\n")
                while True:
                    count += 1
                    terminal_line = input("Enter content line:")

                    file.write(str(count) + " " + terminal_line + "\n")
                    if terminal_line.lower() == "stop":
                        break


if __name__ == "__main__":
    main()
