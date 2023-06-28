import enum
import re
import datetime
from ex1 import SSHLogEntry
import ex2

def to_dictionery(line):
    regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
    match = re.match(regex_pattern, line)
    return {
        'date': datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S'),
        'hostname': match.group(2),
        'id': match.group(3),
        'message': match.group(4)
    }


def to_SSHLogEntry(log):
    log_to_dic = to_dictionery(log)
    regex_pattern = r'error|Accepted|Failed'
    match_error = re.search(regex_pattern, log_to_dic['message'])
    
    if not match_error:
        return ex2.ElseInfo(log, log_to_dic['date'], log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])

    group = match_error.group(0)
    if group == 'error':
        return ex2.Error(log, log_to_dic['date'], log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])
    elif group == 'Accepted':
        return ex2.AcceptedPassword(log, log_to_dic['date'], log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])
    else: 
        return ex2.FailedPassword(log, log_to_dic['date'], log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])


class SSHLogJournal:
    """
    Class represents a list of SSHEntryLogs
    """
    
    def __init__(self, *args) -> None:
        self.logs = []
        for log in args:
            self.logs.append(log)

    def __len__(self):
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)
    
    def __contains__(self, element):
        return element in self.logs
    
    def append(self, log):
        self.logs.append(to_SSHLogEntry(log))

    def get(self, starting_data, end_data):
        logs = []
        for log in self.logs:
            if starting_data < log.date < end_data:
                logs.append(log)
        return logs

    def __str__(self):
        return str(self.logs)