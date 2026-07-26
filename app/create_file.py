import datetime
import sys
import os


def make_file(path: str) -> None:
    current_line = 1
    with open(path, "w") as file:
        current_time = datetime.datetime.now()
        file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            line = input("Enter content line: ")
            if line != "stop":
                file.write(f"{current_line} {line}\n")
                current_line += 1
            else:
                break


if __name__ == "__main__":
    command = sys.argv
    if "-b" in command and "-f" not in command:
        os.makedirs(os.path.join(*command[2:]), exist_ok=True)

    if "-f" in command and "-b" not in command:
        make_file(command[2])

    if "-b" in command and "-f" in command:
        div_path = os.path.join(*command[2:command.index("-f")])
        file_path = div_path + "." + command[command.index("-f") + 1]
        os.makedirs(div_path, exist_ok=True)
        make_file(file_path)
