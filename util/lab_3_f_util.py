import sys
from datetime import datetime, time
from util import regex_matches as rm
from util import is_time_between as itb


def print_logs_between_22_6():
    for line in sys.stdin:
        try:
            matches = rm.get_regex_match(line)
            t = datetime.strptime(matches.group(3), '%H:%M:%S').time()
            if itb.is_time_between(t, time(22, 0, 0), time(6, 0, 0)):
                print(line)

        except Exception as e:
            print(e)
