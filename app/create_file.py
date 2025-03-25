import sys
import os
from datetime import datetime

def create_file():

    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        os.makedirs(os.path.join(os.getcwd(), os.path.join(*sys.argv[2:])), exist_ok= True)

    elif len(sys.argv) > 1 and sys.argv[1] == "-f":
        filename = sys.argv[-1]
        current_time = (datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
        try:
            with open(filename, "a") as file:
                print("Enter content line. Type 'stop' to end")
                while True:
                    user_input = input("")

                    if user_input.lower() == "stop":
                        break
                    file.writelines([f"{current_time}, \n{user_input} + '\n"])

        except Exception as e:
            print(e)
    else:
        print("Pass only one argument")

create_file()