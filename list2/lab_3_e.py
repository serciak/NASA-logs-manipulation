import sys
sys.path.append('../')
from util import lab_3_e_util as l3e


def print_log_with_code_200():
    for line in sys.stdin:
        if l3e.is_code_200(line):
            print(line)


if __name__ == '__main__':
    print_log_with_code_200()
