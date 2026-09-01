from datetime import datetime

import sys
import os


if len(sys.argv) > 0:
    current_mode = None
    path = ""
    file_name = None
    for arg in sys.argv[1:]:
        if arg == "-f":
            current_mode = "create_file"
            continue
        elif arg == "-d":
            current_mode = "create_dir"
            continue

        if current_mode == "create_dir":
            path = os.path.join(path, arg)
            os.makedirs(path, exist_ok=True)

        elif current_mode == "create_file":
            file_name = arg

    if file_name:
        final_path = os.path.join(path, file_name)

        file_exists = os.path.exists(final_path)

        with open(f"{final_path}", "a") as f:
            formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if file_exists:
                f.write("\n")
            f.write(f"{formatted_time}\n")
            counter = 0

            while True:
                counter += 1
                user_input = input("Enter content line: ")
                if user_input.lower() == "stop":
                    break
                f.write(f"{counter} {user_input}\n")
