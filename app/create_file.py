import sys
import os

from datetime import datetime


def check_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def create_input(directory, file_name):
    with open(directory + file_name, "a") as f:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(date_now + "\n")
        counter = 1

        while True:
            input_content = input("Enter content line: ")
            if input_content == "stop":
                f.write("\n")
                break
            else:
                f.write(f"Line{counter} {input_content}\n")
                counter += 1


def create_file():
    if "-d" in sys.argv and "-f" in sys.argv:
        path = check_directory(
            os.sep.join(sys.argv[3:len(sys.argv) - 1]) + os.sep
        )
        file_name = sys.argv[-1]
        create_input(path, file_name)
    elif "-f" in sys.argv:
        path = ""
        file_name = sys.argv[-1]
        create_input(path, file_name)
    elif "-d" in sys.argv:
        path = check_directory(os.sep.join(sys.argv[2:]))
        os.mkdir(path)
        
if __name__ == "__main__":
    create_file()        
