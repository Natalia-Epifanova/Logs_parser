import json

from src.analyzer import analyze_logs


def test_analyze_logs_with_valid_data(tmp_path, test_data):
    """Тестирует анализ логов с корректными данными.

    Проверяет:
        - Корректность чтения и парсинга лог-файла
        - Возвращаемое количество записей
        - Тип возвращаемых данных
        - Сохранение структуры данных
    """

    file_path = tmp_path / "test.log"
    with open(file_path, "w") as f:
        for record in test_data:
            f.write(json.dumps(record) + "\n")

    result = analyze_logs(str(file_path))

    assert len(result) == 3
    assert all(isinstance(record, dict) for record in result)
    assert result[0]["url"] == "/api/context/..."


def test_analyze_logs_with_date_filter(tmp_path, test_data):
    """Тестирует фильтрацию логов по дате.

    Проверяет:
        - Корректность фильтрации записей по указанной дате
        - Количество отфильтрованных записей
        - Сохранение данных после фильтрации
    """
    file_path = tmp_path / "test.log"
    with open(file_path, "w") as f:
        for record in test_data:
            f.write(json.dumps(record) + "\n")

    result = analyze_logs(str(file_path), "2025-06-22")

    assert len(result) == 2
    assert all(isinstance(record, dict) for record in result)
    assert result[1]["url"] == "/api/specializations/..."


def test_analyze_logs_with_missing_file():
    """Тестирует обработку отсутствующего файла.

    Проверяет:
        - Поведение функции при попытке чтения несуществующего файла
        - Возвращаемое значение при ошибке
    """
    result = analyze_logs("some_file.log")
    assert result == []


def test_analyze_logs_with_invalid_data(tmp_path, wrong_test_data):
    """Тестирует обработку логов с некорректными данными.

    Проверяет:
        - Обработку записей с невалидным форматом
        - Количество возвращаемых валидных записей
        - Корректность обработки оставшихся данных
    """
    file_path = tmp_path / "test.log"
    with open(file_path, "w") as f:
        for record in wrong_test_data:
            if isinstance(record, dict):
                f.write(json.dumps(record) + "\n")
            else:
                f.write(record + "\n")

    result = analyze_logs(str(file_path))

    assert len(result) == 2
    assert all(isinstance(record, dict) for record in result)
    assert result[1]["url"] == "/api/specializations/..."
