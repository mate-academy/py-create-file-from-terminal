import os
import sys
import datetime


def create_file(filename: str) -> None:
    count = 0

    with open(filename, "a") as file:
        file.write("\n" + datetime.datetime.now().
                   strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            count += 1
            terminal_line = input("Enter content line: ")
            if terminal_line == "stop":
                file.write("\n")
                break
            if terminal_line.strip():
                file.write(str(count) + " " + terminal_line + "\n")

            else:
                break


def main() -> None:
    flag = sys.argv[1]

    if flag == "-d" and len(sys.argv) >= 3:
        directory_path = os.path.join(*sys.argv[2:])
        os.makedirs(directory_path, exist_ok=True)

    elif flag == "-f" and len(sys.argv) >= 3:
        filename = sys.argv[2]
        current_dir = os.path.dirname(filename)
        create_file(os.path.join(current_dir, filename))

    if "-d" in sys.argv and "-f" in sys.argv and len(sys.argv) == 6:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        if d_index < f_index:
            directory_path = os.path.join(*sys.argv[d_index + 1:f_index - 1])
            os.makedirs(directory_path, exist_ok=True)
            filename = sys.argv[f_index + 1]
            create_file(os.path.join(directory_path, filename))
            return


if __name__ == "__main__":
    main()
