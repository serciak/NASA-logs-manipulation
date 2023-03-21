import sys
sys.path.append('../')
from util import regex_matches as rm
from util import get_file_extension as gfe


def images_ratio():
    image_ext = ['.gif', '.jpg', '.jpeg', '.xbm']
    image_count = 0
    others_count = 0

    for line in sys.stdin:
        try:
            match = rm.get_regex_match(line)
            if gfe.get_file_extension(match) in image_ext:
                image_count += 1
            else:
                others_count += 1
        except Exception as e:
            #print(e)
            pass

    return image_count / others_count

