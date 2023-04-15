import os
import sys
import datetime


def main() -> None:
    dir_names = []
    file_name = ""
    content = ""

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            if i < len(sys.argv) - 1:
                while i + 1 < len(sys.argv) \
                        and not sys.argv[i + 1].startswith("-"):
                    dir_names.extend(sys.argv[i + 1].split(","))
                    i += 1
        elif sys.argv[i] == "-f":
            if i < len(sys.argv) - 1:
                file_name = sys.argv[i + 1]
            i += 1
        i += 1

    nested_dir = ""
    for dir_name in dir_names:
        nested_dir = os.path.join(nested_dir, dir_name)
        os.makedirs(nested_dir, exist_ok=True)

    if file_name and not file_name.startswith("-") and dir_names:
        file_path = os.path.join(nested_dir, file_name)
        with open(file_path, "w") as f:
            # Adding date and time to the file
            now = datetime.datetime.now()
            f.write(f"Creation time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            # Inputting file content
            print(f"Enter content for {file_path} "
                  f"(press Enter on an empty line to finish):")
            while True:
                line = input()
                if line == "stop":
                    break
                content += line + "\n"
            f.write(content)
            f.write("\n")


if __name__ == "__main__":
    main()
