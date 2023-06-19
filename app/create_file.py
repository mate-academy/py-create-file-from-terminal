import datetime
import sys

from os import path, makedirs


def work_with_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        print("Enter content for new_file (Enter 'stop' to finish):")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
        file.write("\n")


def main() -> None:
    terminal_input = sys.argv

    if len(terminal_input) < 2:
        print("Need more arguments!")
        return

    filename = ""
    directory = ""
    try:
        flags = terminal_input[1:]

        if "-d" in flags:
            directories = []
            for argument in range(flags.index("-d") + 1, len(flags)):
                if flags[argument] == "-f":
                    break
                directories.append(flags[argument])
            directory = path.join(*directories)
            makedirs(directory, exist_ok=True)

        if "-f" in flags:
            filename = flags[flags.index("-f") + 1]
        file_path = path.join(directory, filename)
        if not filename:
            print("Please provide the -f flag for the filename.")
            return

        work_with_file(file_path)

    except (IndexError, TypeError, ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
