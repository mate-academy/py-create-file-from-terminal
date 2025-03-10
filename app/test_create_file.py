from pathlib import Path
from unittest.mock import patch
from app.create_file import create_file_or_directory


def test_create_file(tmp_path: Path) -> None:
    # Мокування вводу
    mock_input = [
        "line 1",  # перший рядок
        "line 2",  # другий рядок
        "stop"  # команда для завершення
    ]

    # Запуск функції з мокуванням вводу
    args = ["-f", str(tmp_path / "test_file.txt")]
    with patch("builtins.input", side_effect=mock_input):
        create_file_or_directory(args)

    # Перевірка, чи створений файл
    file_path = tmp_path / "test_file.txt"
    assert file_path.exists()

    # Перевірка вмісту файлу
    with open(file_path, "r") as file:
        content = file.read().splitlines()
    assert len(content) >= 2
    assert content[0] == "line 1"
    assert content[1] == "line 2"
