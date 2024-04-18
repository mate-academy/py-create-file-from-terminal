import subprocess
import tempfile

def test_create_file_script() -> None:
    test_cases = [
        (["python", "create_file.py", "-d", "test_dir", "test_file.txt"], "Test content line 1\nTest content line 2\nstop\n"),
        (["python", "create_file.py", "-f", "test_file.txt"], "Test content line 1\nTest content line 2\nstop\n")
    ]
    
    for cmd_args, input_data in test_cases:
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                process = subprocess.Popen(
                    cmd_args,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=temp_dir,
                    universal_newlines=True
                )
                
                stdout, stderr = process.communicate(input_data)
                
                assert process.returncode == 0, f"Test failed for command: {' '.join(cmd_args)}"
                assert "File created" in stdout, f"Test failed for command: {' '.join(cmd_args)}"
        except Exception as e:
            print(f"Test failed with error: {e}")
            return

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_create_file_script()
