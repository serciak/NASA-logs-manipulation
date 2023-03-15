import sys

from util import regex_matches as rm


def get_log_size_sum():
    size = 0
    for line in sys.stdin:
        try:
            match = rm.get_regex_match(line)
            if match.group(6) != '-':
                size += int(match.group(6))
        except Exception as e:
            print(e)

    return size
