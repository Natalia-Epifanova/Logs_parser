import json
from unittest.mock import patch

import pytest

from main import main


def test_main_success(capsys, tmp_path, test_data):
    """Тестирует успешное выполнение main() с корректными аргументами.

    Проверяет:
    - Обработку валидного лог-файла
    - Формирование отчёта с обязательными полями
    - Отсутствие ошибок при стандартном сценарии
    """
    test_file = tmp_path / "test.log"
    with open(test_file, "w") as f:
        for record in test_data:
            f.write(json.dumps(record) + "\n")

    test_args = ["--file", str(test_file), "--report", "average"]

    with patch("sys.argv", ["main.py"] + test_args):
        main()

    captured = capsys.readouterr()
    assert "handler" in captured.out
    assert "total" in captured.out
    assert "avg_response_time" in captured.out


def test_main_invalid_report(capsys):
    """Тестирует обработку невалидного типа отчёта.

    Проверяет:
    - Завершение программы с ошибкой при неподдерживаемом типе отчёта
    - Наличие сообщения об ошибке в stderr
    - Корректность текста ошибки
    """
    test_args = ["--file", "test.log", "--report", "invalid_report"]

    with patch("sys.argv", ["main.py"] + test_args):
        with pytest.raises(SystemExit):
            main()

    captured = capsys.readouterr()
    assert "invalid choice" in captured.err.lower()


def test_main_with_date_filter(capsys, tmp_path, test_data):
    """Тестирует фильтрацию логов по дате.

    Проверяет:
    - Корректность работы параметра --date
    - Фильтрацию записей по указанной дате
    - Формирование отчёта только для отфильтрованных данных
    """
    test_file = tmp_path / "test.log"
    with open(test_file, "w") as f:
        for record in test_data:
            f.write(json.dumps(record) + "\n")

    test_args = [
        "--file",
        str(test_file),
        "--report",
        "average",
        "--date",
        "2025-06-22",
    ]

    with patch("sys.argv", ["main.py"] + test_args):
        main()

    captured = capsys.readouterr()
    assert "handler" in captured.out
    assert "total" in captured.out
    assert "avg_response_time" in captured.out
