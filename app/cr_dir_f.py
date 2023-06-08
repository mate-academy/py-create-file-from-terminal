import sys
import os
import datetime
def create_dir(path: str = os.getcwd()) -> None:
    os.makedirs(path, exist_ok=True)