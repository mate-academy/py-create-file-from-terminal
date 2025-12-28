from app.create_file import main
import pytest
from pytest import MonkeyPatch
import os

@pytest.mark.parametrize(
    "terminal_arguments, file_path, content",
    [
        (
                ["-d", "hello", "there", "-f", "test_file"],
                "hello/hello/test_file",
                ["1 HI", "2 There"]
        ),
        (
                ["-f", "test_file", "-d", "hello", "there"],
                "hello/hello/test_file",
                ["1 HI", "2 There"]
        ),
    ],
    ids=[
        "-d flag before -f flag",
        "-d flag after -f flag"
    ]
)
def test_create_file(monkeypatch: MonkeyPatch, terminal_arguments: list, file_path: str, content: list[str]):
    inputs = [*content]
    input_messages = []

    def mock_parsed_arguments():
        return terminal_arguments

    def mock_input_content(text):
        input_messages.append(text)
        yield inputs.pop(0)

        if os.path.exists(file_path):
            os.remove(file_path)

    monkeypatch.setattr("sys.argv", mock_parsed_arguments)
    monkeypatch.setattr("builtins.input", mock_input_content)

    main()

    assert input_messages == ["Enter content line: "] * (len(content) + 1)

    assert os.path.exists(file_path)

    with open(file_path, "r") as f:
        assert f.read().splitlines() == content