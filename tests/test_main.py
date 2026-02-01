import os
import shutil
from app.main import main

def test_file_creation_in_current_dir():
    filename = "test_file.txt"
    if os.path.exists(filename):
        os.remove(filename)
    
    import sys
    sys.argv = ["main.py", "-f", filename]
    
    # Симулюємо ввід: рядок 1, рядок 2, stop
    import builtins
    inputs = iter(["line 1", "line 2", "stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.exists(filename), "File should be created"
    with open(filename, "r") as f:
        lines = f.readlines()
        assert len(lines) >= 3, "File should contain timestamp and at least 2 lines"
    os.remove(filename)

def test_directory_and_file_creation():
    dir_path = "new_dir/sub_dir"
    filename = "new_dir/sub_dir/test_file.txt"
    if os.path.exists("new_dir"):
        shutil.rmtree("new_dir")
        
    import sys
    sys.argv = ["main.py", "-d", "new_dir", "sub_dir", "-f", "test_file.txt"]
    
    import builtins
    inputs = iter(["content", "stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.exists(dir_path), "Directories should be created"
    assert os.path.exists(filename), "File should be created inside directories"
    shutil.rmtree("new_dir")
