import os
import sys
import datetime


# handle errors
def error_handling(command: list) -> None:
    if len(command) == 1:
        raise ValueError("Provide commands and dirs and/or file")
    if "-d" not in command and "-f" not in command:
        raise ValueError("Usage: -d <dir> -f <file>")


# check -d directory
def making_directory(
        command: list,
        command_len: int,
        dir_command: str,
        file_command: str
) -> str:
    directory_list = []
    for i in range(command_len):
        if command[i] == dir_command:
            for _ in range(i + 1, command_len):
                if command[_] == file_command:
                    break

                directory_list.append(command[_])

    # create said dir
    directory = os.path.join(os.getcwd(), *directory_list)
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


# check -f file and create
def making_file(
        command: list,
        command_len: int,
        file_command: str,
        directory_string: str
) -> None:
    file_name = None
    for i in range(command_len):
        if command[i] == file_command and i + 1 < command_len:
            file_name = command[i + 1]

    if not file_name:
        raise ValueError("File name not provided after -f")

    file_path = os.path.join(directory_string, file_name)

    # start appending into the file
    count = 1
    with open(file_path, "a") as file_to_write:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file_to_write.write("\n")
        file_to_write.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            user_input = input("Enter content line:")
            if user_input == "stop":
                break
            file_to_write.write(f"{count} {user_input}\n")
            count += 1


if __name__ == "__main__":
    args = sys.argv[1:]
    args_len = len(args)

    error_handling(args)
    if "-d" in args and "-f" not in args:
        dir_string = making_directory(args, args_len, "-d", "-f")
    else:
        dir_string = making_directory(args, args_len, "-d", "-f")
        making_file(args, args_len, "-f", dir_string)
