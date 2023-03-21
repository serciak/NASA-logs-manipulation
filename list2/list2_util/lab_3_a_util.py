import sys
sys.path.append('../')
from util import code_check as cc


def count_codes(wanted_code):
    amount = 0
    for line in sys.stdin:
        if cc.is_wanted_code(line, wanted_code):
            amount += 1

    return amount
