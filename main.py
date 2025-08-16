import argparse

from tabulate import tabulate
from src.analyzer import analyze_logs
from src.reports import generate_average_time_report


def main():
    parser = argparse.ArgumentParser(description='Logs parser')
    parser.add_argument('--file', nargs='+', required=True, help='Путь до файла')
    parser.add_argument('--report', required=True, choices=['average'], help='Type of report')
    parser.add_argument('--date', help='Filter logs by date (YYYY-MM-DD)')

    args = parser.parse_args()

    logs_list = []
    for file_path in args.file:
        logs_list.extend(analyze_logs(file_path, args.date))

    if args.report == 'average':
        report_data = generate_average_time_report(logs_list)
        print(tabulate(report_data, headers=['handler', 'total', 'avg_response_time']))


if __name__ == '__main__':
    main()