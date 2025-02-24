from datetime import datetime


def create_f(file: str) -> None:
    try:
        with open("file", "a", encoding="utf-8") as f:
            print(f"File_name {file} created successfully.")
            print("Input content 'stop' to break loop")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n\n")
            lines = []
            while True:
                line = str(input("Enter content line: "))
                if line.lower() == "stop":
                    break
                lines.append(line)
            for i, line in enumerate(lines, start=1):
                f.write(f"{i}{line}")
                print(f"Adding content to {file}")
    except Exception as e:
        print("Exception", e)
