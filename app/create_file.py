import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    """Parse command line arguments and return directory parts and filename."""
    args = sys.argv[1:]

    if not args:
        print(
            "Error: No arguments provided. "
            "Use -d for directory and/or -f for file."
        )
        sys.exit(1)

    dir_parts = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            # Collect all directory parts until we hit -f or end of args
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            # Next argument should be the filename
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: -f flag requires a filename argument.")
                sys.exit(1)
        else:
            i += 1

    return dir_parts, filename


def create_directory(dir_parts: list[str]) -> str | None:
    """Create directory from parts if it doesn't exist."""
    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return None


def get_content_from_user() -> list[str]:
    """Get content lines from user until exactly 'stop' is entered."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_or_append_file(
        filepath: str, content_lines: list[str]
) -> None:
    """Create or append to file with timestamp and numbered lines."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if file exists and has content
    file_exists = os.path.exists(filepath) and os.path.getsize(filepath) > 0

    with open(filepath, "a", encoding="utf-8") as f:
        # Add exactly one blank line if appending to existing content
        if file_exists:
            # Read the last character to check if file ends with newline
            with open(filepath, "rb") as check_file:
                check_file.seek(-1, 2)  # Go to last byte
                last_char = check_file.read(1)
                ends_with_newline = last_char == b"\n"

            # Write minimal newlines to create exactly one blank line
            if ends_with_newline:
                f.write("\n")  # Just one more newline creates blank line
            else:
                f.write("\n\n")  # Need two: one to end line, one for blank

        # Write timestamp
        f.write(f"{timestamp}\n")

        # Write numbered content lines
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"\nFile created/updated successfully: {filepath}")


def main() -> None:
    dir_parts, filename = parse_arguments()

    # Validate that at least -f flag was provided
    if filename is None:
        if dir_parts:
            # Only -d flag provided, just create directory
            dir_path = create_directory(dir_parts)
            print(f"Directory created: {dir_path}")
        else:
            print("Error: At least -f flag with filename is required.")
            sys.exit(1)
        return

    # Create directory if specified
    dir_path = create_directory(dir_parts)

    # Determine full file path
    if dir_path:
        filepath = os.path.join(dir_path, filename)
    else:
        filepath = filename

    # Get content from user
    content_lines = get_content_from_user()

    # Create or append to file
    create_or_append_file(filepath, content_lines)


if __name__ == "__main__":
    main()
