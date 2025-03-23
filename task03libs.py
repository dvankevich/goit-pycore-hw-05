from datetime import datetime
from pathlib import PurePath, Path
import re

log_levels = {"INFO", "ERROR", "DEBUG", "WARNING"}

def parse_log_line(line: str) -> dict:
    """
    Parses a log line string into a dictionary.

    The function takes a log line in the format:
    'YYYY-MM-DD HH:MM:SS LOGLEVEL Message'
    and extracts the date, time, log level, and message, returning them in a dictionary.

    Args:
        line (str): A single log line string to be parsed.

    Returns:
        dict: A dictionary containing the parsed components of the log line:
            - "date": A string representing the date in 'YYYY-MM-DD' format.
            - "time": A string representing the time in 'HH:MM:SS' format.
            - "loglevel": A string indicating the log level (e.g., "INFO", "ERROR").
            - "message": A string containing the actual log message.
        or empty dict if error
    """
    match = re.match(r'(\S+) (\S+) (\S+) (.+)', line)
    if not match:
        print((f"Log line does not match expected format: {line}"))
        return {}
       
    try:
        # Verify date format
        datetime.strptime(match.group(1), '%Y-%m-%d')
        # Verify time format
        datetime.strptime(match.group(2), '%H:%M:%S')
    except ValueError as e:
        print(f"Invalid date or time: {e}")
        return {}
    
    if match.group(3) not in log_levels:
        print((f"Invalid log level: {match.group(3)}. Expected one of {log_levels}."))
        return {}
     
    return {
        "date": match.group(1),
        "time": match.group(2),
        "loglevel": match.group(3),
        "message": match.group(4)
    }


def load_logs(file_path: str) -> list:
    """
    Loads logs from a specified file and parses each log line into a dictionary.

    The function reads a log file line by line, applies the `parse_log_line` 
    function to each line, and returns a list of dictionaries that represent 
    the parsed log entries.

    Args:
        file_path (str): The path to the log file to be loaded.

    Returns:
        list: A list of dictionaries, where each dictionary contains the parsed
              components of a log entry. Returns an empty list if error.
  
    Example:
        >>> logs = load_logs("/path/to/logfile.log")
        >>> print(logs)
        [{'date': '2024-01-22', 'time': '08:30:01', 'loglevel': 'INFO', 
          'message': 'User logged in successfully'}, ...]
    """

    f_path = Path(file_path)
    if not f_path.exists() or f_path.is_dir() or f_path.stat().st_size == 0:
        return []
    
    log_dict_list = list()

    with open(f_path, "r") as fh:
        for line in fh.readlines():
            log_line = parse_log_line(line)
            if log_line:
                log_dict_list.append(log_line)
            else:
                return []

    return log_dict_list

def filter_logs_by_level(logs: list, level: str) -> list:
    # фільтрація логів логів за рівнем
    if not (level in log_levels):
        return []
    return list(filter(lambda log: log["loglevel"] == level, logs))



def count_logs_by_level(logs: list) -> dict:
    # підрахунок записів за рівнем логування
    counters = {}
    for log in logs:
        log_level = log["loglevel"]
        counters[log_level] = counters.get(log_level, 0) + 1
    return counters

def display_log_counts(counts: dict):
    # форматує та виводить результати. 
    # приймає результати виконання функції count_logs_by_level
    print("Рівень логування| Кількість")
    print("----------------+----------")
    for err_level, count in counts.items():
        print(f"{err_level:<16}|  {count}")


# ToDo створити окрему функцію для тестування функцій
if __name__ == "__main__":
    logline = "2024-01-22 08:30:01 INFO User logged in successfully."
    badLogLine = "2024-01-22T08:30:01 INFO User logged in successfully."
    loglinedict = {"date": "2024-01-22", "time": "08:30:01", "loglevel": "INFO", "message": "User logged in successfully." }

    # https://www.geeksforgeeks.org/how-to-compare-two-dictionaries-in-python/
    assert parse_log_line(logline) == loglinedict, "Dictionaries are not the same!"

    assert load_logs("example.log")[0] == loglinedict
    assert load_logs("noexist.log") == []
    assert load_logs("badformat.log") == []

    example_log = load_logs("example.log")
    assert filter_logs_by_level(example_log, "notInList") == []
    assert len(filter_logs_by_level(example_log, "INFO")) == 4
    assert len(filter_logs_by_level(example_log, "WARNING")) == 1
    assert len(filter_logs_by_level(example_log, "DEBUG")) == 3
    assert len(filter_logs_by_level(example_log, "ERROR")) == 2

    assert count_logs_by_level(example_log) == {'INFO': 4, 'DEBUG': 3, 'ERROR': 2, 'WARNING': 1}

    display_log_counts(count_logs_by_level(load_logs("example.log")))
