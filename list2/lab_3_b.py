import sys
sys.path.append('../')
from list2_util import lab_3_b_util as l3b
from util import convert_bytes


if __name__ == '__main__':
    print("Sum size of log files: ", round(convert_bytes.convert_bytes_to_gb(l3b.get_log_size_sum()), 2), ' GB')
