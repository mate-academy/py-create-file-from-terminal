import os
import sys
from datetime import datetime


def main() -> None:
    command = sys.argv
    if "-d" in command:
        dir_path = os.path.join("/".join(command[2:]))
        os.makedirs(dir_path, exist_ok=True)
    elif "-f" in command:
        name = "".join(command[2:])
        with open(name, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            counter = 0
            while True:
                counter += 1
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                else:
                    file.write(f"{counter} {content}\n")


if __name__ == "__main__":
    main()
