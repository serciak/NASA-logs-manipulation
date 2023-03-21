import sys
import os
import datetime
sys.path.append('../')
from util import regex_matches as rm
from util import get_file_extension as gfe

def convert_values(match):
    domain, date, time, path, code, size = match.groups()
    date = datetime.datetime.strptime(date, '%d/%b/%Y')
    time = datetime.datetime.strptime(time, '%H:%M:%S')
    size = 0 if size == '-' else int(size)

    return domain, date, time, path, int(code), size

def read_log():
    logs = []
    for line in sys.stdin:
        try:
            match = rm.get_regex_match(line)
        except Exception as e:
            pass

        logs.append(convert_values(match))

    return logs

def sort_log(logs, by_elem=0):
    try:
        logs.sort(key=lambda log: log[by_elem])

    except IndexError:
        sys.stderr.write('Index out of range')

def get_entries_by_addr(logs, domain):
    return list(filter(lambda log: log[0] == domain, logs))

def get_entries_by_code(logs, code):
    return list(filter(lambda log: log[4] == code, logs))

def get_entries_by_code_range(logs, min, max):
    return list(filter(lambda log: min <= log[4] <= max, logs))

def get_failed_reads(logs, separate):
    if separate:
        codes_4xx = get_entries_by_code_range(logs, 400, 499)
        codes_5xx = get_entries_by_code_range(logs, 500, 599)

        return codes_4xx, codes_5xx
    else:
        return get_entries_by_code_range(logs, 400, 599)
    
def get_entries_by_extension(logs, ext):
    return list(filter(lambda log: log[3].split(os.extsep)[-1] == ext, logs))
    
def print_entries(logs):
    for log in logs:
        print(log)
