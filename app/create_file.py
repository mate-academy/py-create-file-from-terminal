import sys
from datetime import datetime
from pathlib import Path


def main() -> None:
    args = sys.argv[1:]
    dirs = []
    filename = ""
    current_flag = ""

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        else:
            if current_flag == "-d":
                dirs.append(arg)
            elif current_flag == "-f":
                filename = arg

    full_path = Path(".")
    if dirs:
        full_path = Path(*dirs)
        full_path.mkdir(parents=True, exist_ok=True)

    if filename:
        full_filepath = full_path / filename
        lines = []

        while True:
            user_input = input("Enter content line: ")
            if user_input.strip().lower() == "stop":
                break
            lines.append(user_input)

        if lines:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = current_time + "\n"
            for index, text in enumerate(lines, start=1):
                content += f"{index} {text}\n"

            with open(full_filepath, "a", encoding="utf-8") as file_object:
                file_object.write(content)

            print(f"File created/updated at: {full_filepath}")


if __name__ == "__main__":
    main()
