from typing import List, Dict


def generate_average_time_report(logs_list: List[Dict]) -> List[tuple]:
    """
    Генерация отчета по среднему времени ответа
    На входе список записей лога
    На выходе список кортежей (endpoint, count, avg_time)
    """
    endpoint_statistics = {}

    for record in logs_list:
        endpoint = record.get('url')
        response_time = record.get('response_time')

        if not endpoint or not response_time:
            continue

        if endpoint not in endpoint_statistics:
            endpoint_statistics[endpoint] = {
                'count': 0,
                'total_time': 0
            }

        endpoint_statistics[endpoint]['count'] += 1
        endpoint_statistics[endpoint]['total_time'] += response_time

    report = []
    for endpoint, statistics in endpoint_statistics.items():
        avg_time = statistics['total_time'] / statistics['count']
        report.append((endpoint, statistics['count'], round(avg_time, 3)))

    report.sort(key=lambda x: x[1], reverse=True)

    return report
