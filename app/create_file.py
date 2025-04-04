def write_into_file(our_path: str) -> None:
    # Extracting filename from the command-line arguments based on the -f flag's position
    filename_index = terminal.index("-f") + 1 if "-f" in terminal else -1
    our_path = path.join(our_path, terminal[filename_index])
    line_number = 1  # Initialize line counter
    with open(our_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            file_text = input("Enter content line: ")
            if file_text == "stop":
                break
            # Write each line with a line number
            file.write(f"{line_number} {file_text}\n")
            line_number += 1

def d_and_f_flags() -> None:
    # Adjusting path construction to exclude the filename
    our_path = path.join(*terminal[1:terminal.index("-f")])
    makedirs(our_path, exist_ok=True)  # Ensure directory is created if not exists
    write_into_file(our_path)

def f_flag() -> None:
    # Handling case when only -f flag is passed
    filename = terminal[1] if len(terminal) > 1 else "default.txt"
    our_path = path.join(".", filename)  # Assume current directory if no path provided
    write_into_file(our_path)
