import os
import shutil
from create_file import main

def test_file_creation_in_current_dir():
    filename = "test_file.txt"
    if os.path.exists(filename):
        os.remove(filename)
    
    import sys
    sys.argv = ["create_file.py", "-f", filename]
    
    import builtins
    inputs = iter(["line 1", "line 2", "stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        lines = f.readlines()
        assert len(lines) >= 3
    os.remove(filename)

def test_directory_only_creation():
    dir_path = os.path.join("only_dir", "sub_dir")
    if os.path.exists("only_dir"):
        shutil.rmtree("only_dir")
        
    import sys
    sys.argv = ["create_file.py", "-d", "only_dir", "sub_dir"]
    
    import builtins
    inputs = iter(["stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.isdir(dir_path)
    shutil.rmtree("only_dir")

def test_append_to_existing_file():
    filename = "append_test.txt"
    with open(filename, "w") as f:
        f.write("Initial line\n")
        
    import sys
    sys.argv = ["create_file.py", "-f", filename]
    
    import builtins
    inputs = iter(["new line", "stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    with open(filename, "r") as f:
        content = f.read()
        assert "Initial line" in content
        assert "new line" in content
    os.remove(filename)

def test_cross_platform_path_creation():
    dir_path = os.path.join("cross", "platform")
    filename = os.path.join(dir_path, "file.txt")
    if os.path.exists("cross"):
        shutil.rmtree("cross")
        
    import sys
    sys.argv = ["create_file.py", "-d", "cross", "platform", "-f", "file.txt"]
    
    import builtins
    inputs = iter(["content", "stop"])
    builtins.input = lambda _: next(inputs)
    
    main()
    
    assert os.path.exists(filename)
    shutil.rmtree("cross")
