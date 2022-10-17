import sys
import os
import datetime


def create_file() -> None:
    current_time = datetime.datetime.now()
    print(sys.argv)
    if "-d" in sys.argv:
        for i in range(2, len(sys.argv)):
            if "-f" not in sys.argv[i]:
                os.makedirs(sys.argv[i])
                os.chdir(sys.argv[i])
            else:
                break
    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file_text:
            file_text.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            line = 1

            while True:
                content_file = input("Enter content line: ")
                if content_file == "stop":
                    file_text.write("\n")
                    break
                file_text.write(f"{line} {content_file}\n")
                line += 1


if __name__ == "__main__":
    create_file()
