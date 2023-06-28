import ex1
import ex2
import random
import datetime
from numpy import sort

def get_users_log(logs):
    users = {}
    for line in logs:
        user = ex2.get_user_from_log(line)
        if user:
            if user in users:
                users[user].append(line)
            else:
                users.update({user: [line]})
    return users

def from_dic_to_log(log):
    return log['date'] + " " + log['hostname'] + " [" + log['id'] + "] " + log['message']

def show_random_users_logs(logs):
    nInput = input("Enter the number of logs you wish to see: ")
    while(not nInput.isdigit):
        nInput = input("Enter the number of logs you wish to see: ")
    n = int(nInput)
    users = get_users_log(logs)
    chosen_user = random.choice(list(users))
    users_log = users[chosen_user]
    chosen_logs = set()
    if n < len(users_log):
        for i in range(n):
            log = random.choice(users_log)
            chosen_logs.add(from_dic_to_log(log))
            users_log.remove(log)
    else:
        for i in range(len(users_log)):
            log = random.choice(users_log)
            chosen_logs.add(from_dic_to_log(log))
            users_log.remove(log)
    return chosen_logs
    
def return_datetime(users_date):
    timestamp = datetime.datetime.strptime(users_date)

def mean(time):
    sum = 0
    for t in time:
        sum += t
    if len(time) != 0:
        return sum / len(time)
    else:
        return 0

def to_datetime(users_log):
    for log in users_log:
        log.update({"date":datetime.datetime.strptime(log['date'], '%b %d %H:%M:%S')})
    return sorted(users_log, key=lambda x: x['date'])
    

def user_time(user, users):
    users_logs = to_datetime(users[user])
    log_off_message_type = {'Connection closed', 'Disconnecting', 'session closed', 'preauth'}
    time = []

    start_time = None
    end_time = None

    for log in users_logs:
        message_type = ex2.get_message_type_by_line(log)
        if "Accepted" == message_type:
            start_time = log['date']
        elif (message_type in log_off_message_type) and start_time:
            end_time = log['date']
            diff = end_time-start_time
            min, sec = divmod(diff.days * 24 * 60 * 60  + diff.seconds, 60)
            time.append(min*60+sec)
            start_time = None
            end_time = None
            was_start = False
    return mean(time)
    
def all_users_time(logs):
    users = get_users_log(logs)
    sum = 0
    for user in users:
        sum += user_time(user, users)
    if len(users) != 0:
        return sum/len(users)
    else:
        return 0

def most_active_user(logs):
    users = get_users_log(logs)
    max = -1
    most_active_user = None
    min = 2**31-1
    less_active_user = None
    for user in users:
        number_of_users_activity = 0
        for log in users[user]:
            message = ex2.get_message_type_by_line(log)
            if message == 'Accepted':
                print(message)
                number_of_users_activity += 1
        if number_of_users_activity > max:
            most_active_user = user
            max = number_of_users_activity
        if number_of_users_activity < min:
            less_active_user = user
            min = number_of_users_activity
        print(user + " " + str(number_of_users_activity))
    return less_active_user, most_active_user


if __name__=='__main__':
    logs = [
        {'date': 'Jan  7 14:55:01', 'hostname': 'LabSZ', 'id': '29928', 'message': 'Connection closed user dupa'},
        {'date': 'Jan  7 14:51:01', 'hostname': 'LabSZ', 'id': '29928', 'message': 'Accepted user dupa'}
    ]

    print(all_users_time(logs))
