import os
import sys
import datetime


def content_input() -> list:
    """
           Collect timestamped multiline user input.

           Returns:
               list: First element is a timestamp.
                     Following elements are numbered lines entered by the user
                     (input ends when the user types 'stop').
    """

    content = []

    time_stamp = (datetime.datetime.now().
                  strftime("%Y-%m-%d %H:%M:%S"))

    content.append(time_stamp)

    print("Enter file content line by line, until write stop")
    lines = []
    while True:
        comment = input("Enter content line: ")
        if comment.lower() == "stop":
            break
        lines.append(comment)

    for idx, line in enumerate(lines, start=1):
        content.append(f"{idx} {line}")

    return content


def create_file() -> None:
    """
       Create directories and file from command-line args and append user content.

       Command-line flags:
           -d <dir1 dir2 ...> : one or more directory names (creates full path)
           -f <filename>      : file to create or append content to

       Behavior:
           - creates directories if they don't exist
           - creates file if missing, otherwise appends
           - writes timestamp and user-input lines to the file
    """
    command_line = sys.argv[1:]

    dirs = []
    file_name = None

    # Get names of all dirs
    if "-d" in command_line:
        i = command_line.index("-d") + 1
        while (i < len(command_line)
               and not command_line[i].startswith("-")):
            dirs.append(command_line[i])
            i += 1

    # Get file name
    if "-f" in command_line:
        i = command_line.index("-f") + 1
        if i < len(command_line):
            file_name = command_line[i]

    # Create directories
    if dirs:
        full_dir_path = os.path.join(*dirs)
        os.makedirs(full_dir_path, exist_ok=True)
    else:
        full_dir_path = ""

    # If file name was given, create or append
    if file_name:
        full_file_path = os.path.join(full_dir_path, file_name)

        # Check if file exists
        file_exists = os.path.exists(full_file_path)
        data = content_input()

        with open(full_file_path, "a", encoding="utf-8") as f:
            if file_exists:
                f.write("\n")
            for line in data:
                f.write(line + "\n")
