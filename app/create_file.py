import os
import sys
from datetime import datetime


def create_file(file_path: str, file_name: str) -> None:
    file_path = os.path.join(file_path, file_name)
    date_time = datetime.now()
    text = [date_time.strftime("%Y-%m-%d %H:%M:%F")]
    print("Enter stop to exit")
    count = 1
    while True:
        line = input("Enter new line:")
        if line == "stop":
            break
        text.append(f"{count} {line}")
        count += 1
    if os.path.exists(file_path):
        with open(file_path, "a") as file_new:
            file_new.write("\n")
            for line in text:
                file_new.write(line)
                file_new.write("\n")
    else:
        with open(file_path, "w") as file_new:
            for line in text:
                file_new.write(line)
                file_new.write("\n")


def create_directory(directory_path: list[str]) -> str:
    directory = os.getcwd()
    for i in range(len(directory_path)):
        directory = os.path.join(directory, directory_path[i])
    return directory


def main() -> None:
    command = sys.argv[1:]
    if not command:
        print("No arguments provided. Use -d for directory or -f for file.")
        return
    directory = ""
    if "-d" in command and "-f" in command:
        directory += create_directory(command[command.index("-d") + 1:
                                              command.index("-f")])
        if not os.path.exists(directory):
            os.makedirs(directory)
        create_file(directory, command[command.index("-f") + 1])
    elif "-d" in command:
        directory += create_directory(command[command.index("-d") + 1:])
        if not os.path.exists(directory):
            os.makedirs(directory)
    elif "-f" in command:
        directory += create_directory([])
        create_file(directory, command[command.index("-f") + 1])
    else:
        print("No arguments provided. Use -d for directory or -f for file.")
        return


if __name__ == "__main__":
    main()
