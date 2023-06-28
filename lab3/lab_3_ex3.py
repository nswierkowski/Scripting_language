from datetime import datetime

def entry_to_dict(single_log):
    dic = {
        'ip': single_log[0],
        'datetime': single_log[1],
        '-code': single_log[2],
        'address': single_log[3],
        'requestCode':single_log[4],
        'downloaded': single_log[5]

    }
    return dic

def log_to_dict(logs):
    all_logs = [entry_to_dict(single_log) for single_log in logs]
    host_to_data = {}
    for log in all_logs:
        host = log['ip']
        if host in host_to_data:
            host_to_data.update({host : host_to_data[host]+[log]})
        else:
            host_to_data.update({host : [log]})
    return host_to_data


def get_addrs(logs):
    return [log for log in logs]

def print_dic_entry_dates(logs):
    length = 0
    for key in logs:
        print("-------------------------------------------")
        print(key)
        length = len(logs[key])
        print(str(len))
        if length > 1:
            print("First and last: " + str(logs[key][0]) + ", " + str(logs[key][-1]))
        else:
            print("First and last: " + str(logs[key][0]))
        number_of_200 = 0
        for log in logs[key]:
            if log['requestCode'] == 200:
                number_of_200 += 1
        diff = number_of_200/length
        print("200 to rest: " + str(diff))