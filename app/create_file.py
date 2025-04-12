import os
import sys
from datetime import datetime


def create_flags_list(argv: list) -> dict:
    try:
        flags = {"-d": argv.index("-d"), "-f": argv.index("-f")}
    except ValueError as e:
        if str(e)[1:3] == "-d": flags = {"-f": argv.index("-f")}
        if str(e)[1:3] == "-f": flags = {"-d": argv.index("-d")}
            
    return flags


def make_dir(*args: list) -> None:
    os.makedirs("/".join((args)))
        
        
def create_file_and_content(filename: str) -> None:
    contents = []
    while True:
        content = input("Enter content line: ")
        if content.lower().strip() == "stop":
            break
        contents.append(content)
        
    with open(f"{filename}", "a") as fn:
        fn.write(f"{datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))}\n")
        fn.writelines(contents)
        
if "__main__" == __name__:
    argv = list(sys.argv)
    path = ""
    dictionary = create_flags_list(argv=argv)
    if dictionary.get("-d", False):
        path = argv[dictionary["-d"]+1:dictionary.get("-f", -1)]
        make_dir(*path)
        
    if dictionary.get("-f", False):
        file = argv[dictionary["-f"]+1]
        if path: 
            path += "/";
            path = "/".join(path)
        filename = f"{path}{file}"
        print(filename)
        create_file_and_content(filename=filename)
        
    