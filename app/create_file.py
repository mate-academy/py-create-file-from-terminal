import sys
import os
from datetime import datetime

def create_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created or already exists.")

def get_content_from_user() -> list[str]:
    """Prompts user for content lines until 'stop' is entered."""
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines

def write_to_file(file_path: str, content: list[str]) -> None:
    """Writes content to the specified file with timestamp and numbering."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = [f"{i + 1} {line}" for i, line in enumerate(content)]
    file_exists = os.path.exists(file_path)
    mode = "a" if file_exists else "w"
    with open(file_path, mode, encoding="utf-8") as file:
        if file_exists:
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        file.write("\n".join(numbered_content) + "\n")
    print(f"Content added to '{file_path}'.")

def main() -> None:
    """Main function to parse arguments and execute corresponding actions."""
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dir ...] -f filename")
        return

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
                print("Error: No file name specified after -f.")
                return
        else:
            print(f"Error: Unknown argument '{args[i]}'.")
            return

    target_path = os.path.join(*dir_path) if dir_path else ""
    if target_path:
        create_directory(target_path)

    if file_name:
        file_path = os.path.join(target_path, file_name) if target_path else file_name
        content = get_content_from_user()
        if content:
            write_to_file(file_path, content)
        else:
            print("No content provided. File not created.")

if __name__ == "__main__":
    main()
