import sys
import os
import datetime

def create_file():
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        os.makedirs(os.path.join(os.getcwd(), "/".join(sys.argv[2:])))

    elif len(sys.argv) > 1 and sys.argv[1] == "-f":
        filename = sys.argv[-1]
        current_time = (datetime.datetime.now().isoformat(" ", "seconds"))
        try:
            with open(filename, "a") as file:
                print("Enter content line. Type 'stop' to end")
                while True:
                    user_input = input("")

                    if user_input.lower() == "stop":
                        break
                    file.writelines([f"{current_time}, \n{user_input}"])

        except Exception as e:
            print("Error")
    else:
        print("no")

print(create_file())