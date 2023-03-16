import sys

from util import regex_matches as rm


def get_biggest_asset():
    biggest_asset_size = 0
    biggest_asset = None

    for line in sys.stdin:
        try:
            match = rm.get_regex_match(line)
            if match.group(6) != '-' and int(match.group(6)) > biggest_asset_size:
                biggest_asset = match
                biggest_asset_size = int(match.group(6))
        except Exception as e:
            #print(e)
            pass

    return biggest_asset
