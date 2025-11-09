import sys
import os
import datetime


def args_parser() -> tuple[list[str], str | None]:
    if not (args := sys.argv[1:]):
        raise ValueError("No arguments provided")

    if "-d" not in args and "-f" not in args:
        raise ValueError(
            "You must provide at least one flag: -d or -f"
        )

    if args.count("-f") > 1 or args.count("-d") > 1:
        raise ValueError("Duplicate flags are not allowed")

    def after_flag(flag: str) -> list[str]:
        if flag not in args:
            return []
        start = args.index(flag) + 1
        for arg_index in range(start, len(args)):
            if args[arg_index].startswith("-"):
                return args[start:arg_index]
        return args[start:]

    dirs = after_flag("-d")
    filename = after_flag("-f")

    if "-f" in args and not filename:
        raise ValueError("Missing file name after -f")
    if "-d" in args and not dirs:
        raise ValueError("Missing directories after -d")
    if (
        "-d" in args
        and "-f" in args
        and args.index("-f") < args.index("-d")
    ):
        raise ValueError("-f cannot appear before -d")
    if len(filename) > 1:
        raise ValueError(
            "You can specify only one file after -f"
        )

    return dirs, filename[0] if filename else None


def validate_names(dirs: list[str], filename: str | None) -> None:
    for name in [*dirs, filename] if filename else dirs:
        if chars := set(name) & set('<>:\"/\\|?*'):
            raise ValueError(
                f"Invalid characters: '{chars}' in name: '{name}'"
            )


def main() -> None:
    dirs, filename = args_parser()
    validate_names(dirs, filename)

    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)

    if filename:
        path = os.path.join(*dirs, filename) if dirs else filename
        with open(path, "a") as file:
            file.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n"
            )
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1

            file.write("\n")


if __name__ == "__main__":
    main()
