import sys
sys.path.append('../')

from list2_util import lab_3_h_util as l3h


def print_logs_pl():
    for line in sys.stdin:
        if l3h.is_pl(line):
            print(line)


if __name__ == '__main__':
    print_logs_pl()
