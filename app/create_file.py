import sys
import os
import datetime


def create_file(directory: str, content: list[str]) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(directory, "a") as file:
        file.write(current_time + "\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")
        file.write("\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Python create_file.py -d directory_path -f file_name")
        return

    if "-d" in sys.argv and "-f" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory_path = os.path.join(*sys.argv[directory_index:
                                                file_index - 1])
        file_name = sys.argv[file_index]
        directory = os.path.join(directory_path, file_name)
        os.makedirs(directory_path, exist_ok=True)
    elif "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory_path = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory_path, exist_ok=True)
        return
    elif "-f" in sys.argv:
        directory = sys.argv[sys.argv.index("-f") + 1]
    else:
        print("Invalid. Use -d for directory or -f for file.")
        return

    content = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(directory, content)
    print(f"File '{directory}' created successfully.")


if __name__ == "__main__":
    main()
