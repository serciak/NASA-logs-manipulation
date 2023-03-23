import sys
sys.path.append('../')
import datetime

def entry_to_dict(log):
    log_dict = {'ip': log[0], 
                'date': log[1],
                'time': log[2],
                'path': log[3],
                'code': log[4],
                'size': log[5]}
    
    return log_dict

def log_to_dict(logs):
    logs_dict = {}

    for log in logs:
        if log[0] in logs_dict:
            logs_dict[log[0]].append(entry_to_dict(log))
        else:
            logs_dict[log[0]] = [entry_to_dict(log)]

    return logs_dict

def get_addrs(logs_dict):
    return list(logs_dict.keys())

def get_host_data(logs):
    requests_num = 0
    code_200_num = 0
    first_date = datetime.datetime.max
    last_date = datetime.datetime.min

    for log in logs:
        requests_num += 1
        code_200_num += 1 if log['code'] == 200 else 0

        log_time = datetime.datetime.combine(log['date'].date(), log['time'].time())
        first_date = log_time if log_time < first_date else first_date
        last_date = log_time if log_time > last_date else last_date

    return requests_num, first_date, last_date, round(code_200_num/requests_num, 2)


def print_dict_entry_dates(logs_dict):
    for k, v in logs_dict.items():
        host_data = get_host_data(v)
        print(f'host: {k:<40}\treq num: {host_data[0]:<3}\tstart: {host_data[1]}\tend: {host_data[2]}\t200 to other ratio: {host_data[3]}')



