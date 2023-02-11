from datetime import datetime


def writer_text(
        pathfile: str,
        command: str = "a",
        number_line: int = 1
) -> None:
    with open(pathfile, command) as file_out:
        if command != "w":
            file_out.write("\n")
        now = datetime.now()

        file_out.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            some_text = input("Enter content line: ")
            if some_text == "stop":
                break
            file_out.write(f"{number_line} {some_text}\n")
            number_line += 1
