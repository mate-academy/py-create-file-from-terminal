import sys
import os
import datetime


def create_file(directory: str, content: list[str]) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(directory, "a") as file:
        file.write(current_time + "\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Python create_file.py -d directory_path -f file_name")
        return

    if sys.argv[1] == "-d":
        directory_path = os.path.join(*sys.argv[2:-2])
        os.makedirs(directory_path, exist_ok=True)
        file_name = sys.argv[-1]
        directory = os.path.join(directory_path, file_name)
    elif sys.argv[1] == "-f":
        directory = sys.argv[2]
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
