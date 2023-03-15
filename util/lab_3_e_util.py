from util import code_check as cc


def is_code_200(line):
    try:
        if cc.is_wanted_code(line, '200'):
            print(line)

    except Exception as e:
        print(e)
