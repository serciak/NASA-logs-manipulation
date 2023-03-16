from util import regex_matches as rm


def is_wanted_code(line, wanted_code):
    try:
        match = rm.get_regex_match(line)
        if match.group(5) == wanted_code:
            return True
        else:
            return False
    except Exception as e:
        #print(e)
        pass
