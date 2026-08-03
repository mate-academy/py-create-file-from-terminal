from datetime import datetime
import sys
import os


def create_file() -> None:
    command = sys.argv[1:]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dir_args = []
    if "-d" in command:
        d_index = command.index("-d")
        for arg in command[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_args.append(arg)

    dir_path = None
    if dir_args:
        dir_path = os.path.join(*dir_args)
        os.makedirs(dir_path, exist_ok=True)

    file_name = None
    if "-f" in command:
        f_index = command.index("-f")
        if (
            f_index + 1 < len(command)
            and not command[f_index + 1].startswith("-")
        ):
            file_name = command[f_index + 1]

    if file_name:
        file_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )
        file_exists = os.path.exists(file_path)
        with open(file_path, "a") as f:
            file_content = []
            line = 1
            while True:
                line_content = input("Enter content line: ")
                if line_content == "stop":
                    break
                file_content.append(f"{line} {line_content}")
                line += 1
            if file_exists:
                f.write("\n")
            f.write(current_time + "\n")
            f.write("\n".join(file_content) + "\n")


create_file()
