import os, sys
from pathlib import PurePath, Path
import re

# ToDo - додати перевірки корректності формату рядка
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
    """
    match = re.match(r'(\S+) (\S+) (\S+) (.+)', line)
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
        >>> logs = load_logs("path/to/logfile.log")
        >>> print(logs)
        [{'date': '2024-01-22', 'time': '08:30:01', 'loglevel': 'INFO', 
          'message': 'User logged in successfully'}, ...]
    """

    f_path = Path(file_path)
    if not f_path.exists() or f_path.is_dir() or f_path.stat().st_size == 0:
        return []
    
    log_dict_list = list()

    # Додав обробник file exceptions.
    # файл може стати недоступним під час читання
    # https://www.geekster.in/articles/python-file-exception/
    # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
    try:
        with open(f_path, "r") as fh:
            for line in fh.readlines():
                log_dict_list.append(parse_log_line(line))
    except Exception as e:
        print(f"Error reading log file: {e}")

    return log_dict_list

def filter_logs_by_level(logs: list, level: str) -> list:
    # фільтрація логів логів за рівнем
    pass

def count_logs_by_level(logs: list) -> dict:
    # підрахунок записів за рівнем логування
    pass

def display_log_counts(counts: dict):
    # форматує та виводить результати. 
    # приймає результати виконання функції count_logs_by_level
    pass



if __name__ == "__main__":
    logline = "2024-01-22 08:30:01 INFO User logged in successfully."
    badLogLine = "2024-01-22T08:30:01 INFO User logged in successfully."
    loglinedict = {"date": "2024-01-22", "time": "08:30:01", "loglevel": "INFO", "message": "User logged in successfully." }

    print(parse_log_line(logline))
    # https://www.geeksforgeeks.org/how-to-compare-two-dictionaries-in-python/
    assert parse_log_line(logline) == loglinedict, "Dictionaries are not the same!"
    # print(parse_log_line(badLogLine))

    print(load_logs("example.log")[0])
    assert load_logs("example.log")[0] == loglinedict
    assert load_logs("noexist.log") == []