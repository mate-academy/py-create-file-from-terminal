from datetime import datetime


def create_file(filename: str) -> None:
    try:
        with open(filename, "a") as file:
            print(f"File '{filename}' created successfully.")
            print("Input content (type 'stop' to finish):")
            current_date = datetime.now().strftime("%Y/%B/%d %I:%M:%S")
            content = f"{current_date}\n"
            while True:
                line = str(input())
                if line.lower() == "stop":
                    break
                content += line + "\n"
            file.write(content)
            print(f"Content written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")