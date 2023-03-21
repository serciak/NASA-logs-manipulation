import sys
sys.path.append('../')
from lab_2 import *
from lab_3 import *


if __name__ == '__main__':
    logs = read_log()
    logs = log_to_dict(logs)
    print_dict_entry_dates(logs)