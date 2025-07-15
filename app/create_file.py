import sys
import os
import datetime


def main() -> None:
    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")

        if f_index + 1 < len(sys.argv):
            file_name = sys.argv[f_index + 1]
            print("File for create:", file_name)
        else:
            print("Error: after -f must be file name")
    else:
        print("Error: no -f")
        sys.exit()

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        path_parts = sys.argv[d_index + 1 : f_index]
        folder_path = os.path.join(*path_parts)
        os.makedirs(folder_path, exist_ok=True)
        file_name = os.path.join(folder_path, file_name)

    content_lines = []
    while True:
        user_text = input("Enter content line: ")
        if user_text == "stop":
            break
        content_lines.append(user_text)

    with open(file_name, "a") as f:
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(time_str + "\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")


if __name__ == "__main__":
    main()
