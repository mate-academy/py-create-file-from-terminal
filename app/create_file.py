import os
import argparse
from datetime import datetime


invalid_chars = r'<>:"/\\|?*'


def validate_name(name: str) -> None:
    if len(name) > 255:
        raise ValueError(f"Name '{name}' is too long")
    if any(char in invalid_chars for char in name):
        raise ValueError(f"Name '{name}' has invalid characters")
    if name in {".", ".."}:
        raise ValueError(f"Name '{name}' is not allowed")
    if name.endswith(" ") or name.endswith("."):
        raise ValueError(f"Name '{name}' cannot end with space or dot")


def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create files and directories"
    )
    parser.add_argument("-d", nargs="+", help="Directory to create")
    parser.add_argument("-f", help="File to create")
    return parser.parse_args()


if __name__ == "__main__":
    try:
        args = create_parser()
        if args.d:
            for directory in args.d:
                validate_name(directory)

            dir_path = os.path.join(*args.d)
            os.makedirs(dir_path, exist_ok=True)

        if args.f:
            validate_name(args.f)

            file_path = args.f
            if args.d:
                file_path = os.path.join(*args.d, args.f)

            with open(file_path, "a", encoding="utf-8") as file:
                if os.path.getsize(file_path) != 0:
                    file.write("\n")

                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(time_now + "\n")

                string_count = 1
                while True:
                    user_input = input("Enter content line: ")

                    if user_input == "stop":
                        break

                    file.write(f"{string_count} {user_input}\n")
                    string_count += 1

    except PermissionError as e:
        print("PermissionError:", e)
    except OSError as e:
        print("OSError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Unexpected error:", e)
