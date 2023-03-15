import sys
from datetime import datetime, time
from util import regex_matches as rm
from util import is_time_between as itb


def is_pl(line):
    try:
        matches = rm.get_regex_match(line)
        domain = matches.group(1).split(sep='.')[-1]
        return domain == 'pl'

    except Exception as e:
        print(e)
