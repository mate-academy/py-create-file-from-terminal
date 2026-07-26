from datetime import datetime


def write_data_to_file(file_path: str, lines: list[str]) -> None:
    header = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "w") as file:
        file.write(header + "\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i}. {line}\n")
