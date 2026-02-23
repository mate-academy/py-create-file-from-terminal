def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
            i += 2
        else:
            i += 1

    if directory_parts:
        dir_path = os.path.join(*directory_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name is None:
        return

    file_path = os.path.join(dir_path, file_name)

    content_lines = get_content_lines()

    if not content_lines:
        return

    timestamp = get_timestamp()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")