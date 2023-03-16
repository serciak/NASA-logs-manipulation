import sys
from datetime import datetime, time
from util import regex_matches as rm
from util import is_time_between as itb


def is_friday(line):
    try:
        matches = rm.get_regex_match(line)
        d = datetime.strptime(matches.group(2), '%d/%b/%Y')
        return datetime.weekday(d) == 4

    except Exception as e:
        #print(e)
        pass
