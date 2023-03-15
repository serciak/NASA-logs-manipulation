import sys

from util import code_check as cc


def print_log_with_code_200():
    for line in sys.stdin:
        try:
            if cc.is_wanted_code(line, '200'):
                print(line)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    print_log_with_code_200()
