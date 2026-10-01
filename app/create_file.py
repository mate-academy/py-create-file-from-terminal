import sys
import os
from datetime import datetime


def main() -> None:
    dirs = []
    filename = None
    current_flag = None

    arg_index = 1
    while arg_index < len(sys.argv):
        arg = sys.argv[arg_index]

        if arg == "-d":
            current_flag = "d"
        elif arg == "-f":
            current_flag = "f"
        elif current_flag == "d":
            dirs.append(arg)
        elif current_flag == "f":
            filename = arg

        arg_index += 1

    if not filename and dirs:
        caminho_completo = os.path.join(*dirs)
        os.makedirs(caminho_completo, exist_ok=True)
        return

    if not filename:
        print("Error: -f flag is required")
        sys.exit(1)

    caminho_completo = os.path.join(*dirs) if dirs else "."
    os.makedirs(caminho_completo, exist_ok=True)

    lines = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(content)

    file_path = os.path.join(
        caminho_completo, filename) if caminho_completo != "." else filename

    with open(file_path, "a") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


if __name__ == "__main__":
    main()
