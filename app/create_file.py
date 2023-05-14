import sys
from creation import create_file, create_dir


command = sys.argv

if "-f" in command and "-d" not in command:
    create_file(command)

if "-d" in command and "-f" not in command:
    create_dir(command)

if "-f" in command and "-d" in command:
    create_file(command, create_dir(command))
