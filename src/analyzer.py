import json
from typing import Dict, List, Optional


def analyze_logs(file_path: str, filter_date: Optional[str] = None) -> List[Dict]:
    """
    Чтение и анализ лог-файла
    На вход подаются путь до файла и дата для фильтрации
    На выходе список записей лога
    """
    logs_list = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    record = json.loads(line)
                    if filter_date:
                        date_in_file = str(record.get("@timestamp"))[0:10]
                        if date_in_file != filter_date:
                            continue
                    logs_list.append(record)
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    return logs_list
