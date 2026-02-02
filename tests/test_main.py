import os
import shutil
import pytest
import sys

# Додаємо папку app до шляхів пошуку модулів
sys.path.append(os.path.join(os.getcwd(), "app"))
from create_file import main

def test_file_creation_with_append():
    filename = "test_append.txt"
    if os.path.exists(filename):
        os.remove(filename)
    
    sys.argv = ["create_file.py", "-f", filename]
    import builtins
    inputs = iter(["line 1", "stop"])
    builtins.input = lambda _: next(inputs)
    main()
    
    inputs = iter(["line 2", "stop"])
    builtins.input = lambda _: next(inputs)
    main()
    
    with open(filename, "r") as f:
        content = f.read()
        assert "line 1" in content
        assert "line 2" in content
    os.remove(filename)

def test_directory_only_creation():
    dir_path = os.path.join("test_dir", "sub_dir")
    if os.path.exists("test_dir"):
        shutil.rmtree("test_dir")
        
    sys.argv = ["create_file.py", "-d", "test_dir", "sub_dir"]
    import builtins
    inputs = iter(["stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.isdir(dir_path)
    shutil.rmtree("test_dir")
