import sys, argparse
from pathlib import PurePath, Path
from task03libs import display_log_counts, count_logs_by_level, load_logs, filter_logs_by_level

def main():
    parser = argparse.ArgumentParser(
        description='Log file analizer.')
    # Required arguments
    parser.add_argument('file', help='The log file')

    # Optional argument with choices
    parser.add_argument('-l', '--loglevel', choices=['INFO', 'ERROR', 'DEBUG', 'WARNING'], help='The log level. If not specified, all messages are displayed')

    parser.epilog = f'Example usage:\n  python {parser.prog} logfile.log --loglevel DEBUG\n'

    # Parse the command line arguments
    args = parser.parse_args()

    logs = load_logs(args.file)

    if not logs:
        print(f"File {args.file} not found or incorrect format.")
        sys.exit(2) # No such file or directory

    if args.loglevel == None:
        display_log_counts(count_logs_by_level(logs))
        sys.exit()

    filtered_logs = filter_logs_by_level(logs, args.loglevel)
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} {log['loglevel']} {log['message']}")

    sys.exit()

if __name__ == "__main__":
    main()