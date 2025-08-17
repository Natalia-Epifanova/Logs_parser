from src.reports import generate_average_time_report


def test_generate_average_time_report_with_valid_data(test_data_for_report):
    """Тестирует генерацию отчёта с корректными данными.

    Проверяет:
        - Количество возвращаемых записей в отчёте
        - Корректность расчёта среднего времени
    """
    result = generate_average_time_report(test_data_for_report)

    assert len(result) == 3
    assert result[0] == ("/api/context/...", 3, 0.028)


def test_generate_average_time_report_with_invalid_data(wrong_test_data_for_report):
    """Тестирует генерацию отчёта с частично некорректными данными.

    Проверяет:
        - Обработку записей с отсутствующими полями
        - Корректность расчётов при неполных данных
        - Количество возвращаемых записей
    """
    result = generate_average_time_report(wrong_test_data_for_report)

    assert len(result) == 2
    assert result[0] == ("/api/context/...", 2, 0.022)
