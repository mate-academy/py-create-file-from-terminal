import datetime
import os


def create_file_with_content(command: list):
    with os.popen(command[-1], "w") as new_f:
        result = []
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        result.append(date_time)
        content = input("Enter content line: ")
        num_line = 1
        if content != "stop":
            content = f"{num_line} " + content
            result.append(content)
            num_line += 1
        while content != "stop":
            content = input("Enter content line: ")
            if content != "stop":
                content = f"{num_line} " + content
                result.append(content)
                num_line += 1
        result = "\n".join(result)
        new_f.writelines(result)
