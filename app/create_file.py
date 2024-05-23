import datetime
import sys
import os


def input_strings() -> list:  
    str, num, lines = "", 0, []
    while True:
        str = input("Enter content line: ")
        if str == "stop":
           break
        num += 1
        lines.append(f"\n{num} {str}")
    return lines    

def parsing_file_and_directories() -> dict:
    file, dirs = 0, 0
    for i, arg in enumerate(sys.argv):
        if arg == "-f":
            file = i + 1
        if arg == "-d":
            dirs = i + 1
    
    if file:
        file_str = sys.argv[file] 
    else:
        file_str = ""

    if file and dirs and file > dirs:
         dir_list = sys.argv[dirs : file - 1]
    elif (file and dirs and file < dirs) or (not file and dirs):
         dir_list = sys.argv[dirs : ]
    
    return {"file" : file_str, "dirs" : dir_list}

def create_directories(dirs_name: list) -> str:
    new_path = ""
    parent_dir = os.getcwd()
    if dirs_name:
        mode = 0o666
        new_path = parent_dir

    for dir_name in dirs_name:
        new_path = os.path.join(new_path, dir_name.strip())
    os.makedirs(new_path, mode)
    
    return new_path


new_path = os.getcwd()
params = parsing_file_and_directories()
print(params)

if params["dirs"]:
    new_path = create_directories(params["dirs"])

print(new_path)

if params["file"]:
    full_path = os.path.join(new_path, params["file"])
    with open(full_path, "a") as f:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{date_str}")
        f.writelines(input_strings())
