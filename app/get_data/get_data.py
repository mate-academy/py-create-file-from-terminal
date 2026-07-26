
def get_file_content_from_user() -> list[str]:
    lines = []

    while True:
        user_input = input("Enter content line: ")

        if user_input.lower() == "stop":
            break
        else:
            lines.append(user_input)

    return lines
