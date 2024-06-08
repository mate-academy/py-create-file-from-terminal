import os
import sys
import datetime
from optparse import OptionParser

def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        f.write(f"{time_now}\n")
        
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line}\n")

def create_dir(path: str, file_name: str) -> None:
    if file_name:
        if path:
            if not os.path.isdir(path):
                os.makedirs(path)
            file_path = os.path.join(path, file_name)
            create_file(file_path)
        else:
            create_file(file_name)
    else:
        print("No filename provided.")

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", dest="filename")
    parser.add_option("-d", dest="dir_name")
    (options, args) = parser.parse_args(sys.argv)
    create_dir(options.dir_name, options.filename)
