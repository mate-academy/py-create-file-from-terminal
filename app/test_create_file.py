from unittest.mock import patch
from datetime import datetime  # Додаємо імпорт datetime
from create_file import create_file_or_directory  # Заміни на правильний імп


def test_create_file(tmp_path: list[str]) -> None:
    """Перевіряє, чи створюється файл з правильним вмістом."""
    test_file = tmp_path / "test.txt"
    input_lines = ["Line1 content", "Line2 content", "Line3 content"]

    # Мокаємо input, щоб замінити його на попередньо визначений список рядків
    with patch("builtins.input", side_effect=input_lines + ["stop"]):
        create_file_or_directory(["create_file.py", "-f", str(test_file)])

    assert test_file.exists()

    # Перевіряємо вміст файлу
    with open(test_file, "r") as f:
        content = f.readlines()

    assert len(content) >= 3
    # Має бути щонайменше 3 рядки (дата + 2 рядки + stop)
    assert datetime.strptime(content[0].strip(), "%Y-%m-%d %H:%M:%S")
    # Перевірка формату дати
    assert content[1].strip().startswith("1 Line1 content")
    assert content[2].strip().startswith("2 Line2 content")
    assert content[3].strip().startswith("3 Line3 content")
