import os
import sys
import datetime


def create_file_from_terminal() -> None:
    params = sys.argv[1:]

    path = ""

    if "-d" in params:
        d_flag_index = params.index("-d")
        d_flag_params = []

        for param in params[d_flag_index + 1 :]:
            if param.startswith("-"):
                break
            d_flag_params.append(param)

        path = os.path.join(*d_flag_params)
        os.makedirs(path, exist_ok=True)
        path += "/"

    if "-f" in params:
        f_flag_index = params.index("-f")
        path += params[f_flag_index + 1]

        file_exists = os.path.exists(path)

        with open(path, "a+") as f:
            if file_exists:
                f.write("\n")
            f.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
            count = 1
            while True:
                line_message = input("Enter content line: ")
                if line_message.lower() == "stop":
                    break
                f.write(f"{count} {line_message}" + "\n")
                count += 1


create_file_from_terminal()
