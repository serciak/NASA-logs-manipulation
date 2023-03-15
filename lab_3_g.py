import sys

from util import lab_3_g_util as l3g


def print_logs_friday():
    for line in sys.stdin:
        if l3g.is_friday(line):
            print(line)


if __name__ == '__main__':
    print_logs_friday()
