import sys


def print_logs():
    for line in sys.stdin:
        print(line)


if __name__ == '__main__':
    print_logs()
