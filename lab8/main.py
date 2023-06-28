from SSHLogJournalClass import SSHLogJournal
from User import SSHUser
import datetime

def read(file):
    log_list = SSHLogJournal()
    with open(file) as f:
        for line in f:
            log_list.append(line)
    return log_list
            
if __name__=='__main__':
    logs = read('SSH.log')

    user1 = SSHUser('user1', datetime.datetime(2023, 12, 1, 12, 24, 54))
    user2 = SSHUser('user2', datetime.datetime(2019, 1, 24, 6, 12, 5))
    user3 = SSHUser('user3', datetime.datetime(2022, 4, 12, 23, 49, 4))
    user4 = SSHUser('user4', datetime.datetime(2022, 7, 30, 14, 24, 54))
    
    positive_to_validate = [user1, user2, user3, user4]
    positive_to_validate += logs.get(datetime.datetime(1900, 1, 7, 6, 0, 0), datetime.datetime(1900, 1, 7, 15, 0, 0))
    for log in positive_to_validate:
        print(log.validate())


