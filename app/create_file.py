import sys
import os
from datetime import datetime


def get_content_lines() -> list[str]:
    lines = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def main() -> None:
    args = sys.argv[1:]

    dir_path = ""
    file_name = ""
    content = []

    if "-d" in args:
        d_index = args.index("-d")
        i = d_index + 1
        while i < len(args) and args[i] not in ["-f"]:
            dir_path = os.path.join(dir_path, args[i])
            i += 1
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Brakuje nazwy pliku po -f")
            return

        content = get_content_lines()

        full_path = os.path.join(dir_path,
                                 file_name) if dir_path else file_name

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_text = f"\n{timestamp}\n" + "\n".join(content) + "\n"

        with open(full_path, "a", encoding="utf-8") as f:
            f.write(full_text)

        print(f"Zapisano do pliku: {full_path}")

    elif "-d" in args:
        print(f"Utworzono katalog: {dir_path}")

    else:
        print("Użyj -d do katalogu lub -f do pliku lub obu naraz.")


if __name__ == "__main__":
    main()
