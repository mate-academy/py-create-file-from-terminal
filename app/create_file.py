import sys
import os
from datetime import datetime

def create_directory(path_parts):
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path

def get_file_content():
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines

def write_to_file(file_path, content_lines):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")
    
    print(f"Content written to {file_path}")

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: python create_file.py -d <dir_path> -f <file_name>")
        sys.exit(1)
    
    dir_path = []
    file_name = None
    
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    
    if dir_path:
        dir_full_path = create_directory(dir_path)
    else:
        dir_full_path = os.getcwd()
    
    if file_name:
        file_path = os.path.join(dir_full_path, file_name)
        content = get_file_content()
        write_to_file(file_path, content)
    else:
        print("No file name provided.")
        sys.exit(1)
    
if __name__ == "__main__":
    main()
