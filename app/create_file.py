import os
import sys
import datetime as dt
from pathlib import Path


def create_file() -> None:
    terminal_command = sys.argv

    cwd = Path.cwd()

    if "-d" in terminal_command:
        idx_d = terminal_command.index("-d")
        folders = (terminal_command[idx_d + 1:])
        if "-f" in folders:
            folders = folders[:folders.index("-f")]
            # if len(folders) > 1:
            #     folders = (folders.strip()).replace(" ", "/")
        full_path = str(os.path.join(cwd, *folders)).strip()
        try:
            os.makedirs(full_path, exist_ok=True)
        except OSError:
            print("Creation of the directory %s failed" % full_path)
    else:
        full_path = cwd

    if "-f" in terminal_command:
        idx_f = terminal_command.index("-f")
        try:
            filename = os.path.join(
                full_path,
                terminal_command[idx_f + 1])

            with open(filename, "a") as file:
                datetimestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\n{datetimestamp}\n")

                line_nbr = 1
                while True:
                    line = input("Enter content ('stop' to exit) "
                                 f"({line_nbr}): ")
                    if line.lower() == "stop":
                        break
                    file.write(f"{line_nbr} {line}\n")
                    line_nbr += 1

        except IndexError:
            print("File name is missing")
        except Exception as e:
            print(f"Error: Failure when creating file: {e}")


if __name__ == "__main__":
    create_file()
