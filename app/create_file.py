import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if "-d" not in args and "-f" not in args:
        print("Error: You must specify at least one flag (-d or -f).")
        return

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for part in args[d_index + 1:]:
            if part.startswith("-"):
                break
            dir_parts.append(part)

        if dir_parts:
            dir_path = os.path.join(*dir_parts)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created: {dir_path}")
        else:
            print("Error: No directory specified after -d flag.")
            return
    else:
        dir_path = ""

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: No file name specified after -f flag.")
            return

        if not dir_path:
            file_path = file_name
        else:
            file_path = os.path.join(dir_path, file_name)

        # Creating or appending to the file
        with open(file_path, "a+") as file:
            print(f"File opened: {file_path}")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")

            line_count = 1
            while True:
                content = input(f"Enter content line ({line_count}): ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_count} {content}\n")
                line_count += 1

            print(f"Content written to: {file_path}")
    else:
        if not dir_path:
            print("Error: You must specify the -f flag to create a file.")


if __name__ == "__main__":
    main()
