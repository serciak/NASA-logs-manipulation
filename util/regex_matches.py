import re


def get_regex_match(log):
    log_regex1 = re.compile(r'^(\S+) \S+ \S+ \[(\d{2}/\w{3}/\d{4}):(\d{2}:\d{2}:\d{2}) [-+]\d{4}\]'
                           r' "(?:[A-Z]+ )?([^\s"]*)(?:\s+\S*){0,3}" (\d{3}) (\d+|-)$')
    log_regex2 = re.compile(r'^(\S+) \S+ \S+ \[(\d{2}/\w{3}/\d{4}):(\d{2}:\d{2}:\d{2}) [-+]\d{4}\]'
                           r' "(?:[A-Z]+ )?([^\s"]*)(?:\s+\S*)*" (\d{3}) (\d+)$')

    match1 = log_regex1.match(log)
    match2 = log_regex2.match(log)

    if match1 is not None:
        return match1
    if match2 is not None:
        return match2

    raise Exception('Incorrect log formatting')
