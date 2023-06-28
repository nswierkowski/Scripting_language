import enum
import re
import datetime
from ex1 import SSHLogEntry
import ex2
from typing import Iterator, List, Dict, Optional, Union

def to_dictionery(line : str) -> Dict[str, str]:
    regex_pattern: str = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
    match: Optional[re.Match[str]]  = re.match(regex_pattern, line)
    if not match:
        return {}
    return {
        #'date': datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S'),
        'date': match.group(1),
        'hostname': match.group(2),
        'id': match.group(3),
        'message': match.group(4)
    }


def to_SSHLogEntry(log : str) -> SSHLogEntry:
    log_to_dic: Dict[str, str] = to_dictionery(log)
    regex_pattern: str = r'error|Accepted|Failed'
    match_error: Optional[re.Match[str]] = re.search(regex_pattern, log_to_dic['message'])
    date: datetime.datetime = datetime.datetime.strptime(log_to_dic['date'], '%b %d %H:%M:%S')

    if not match_error:
        return ex2.ElseInfo(log, date, log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])

    group: str = match_error.group(0)
    if group == 'error':
        return ex2.Error(log, date, log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])
    elif group == 'Accepted':
        return ex2.AcceptedPassword(log, date, log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])
    else: 
        return ex2.FailedPassword(log, date, log_to_dic['hostname'], log_to_dic['message'], log_to_dic['id'])


class SSHLogJournal:
    """
    Class represents a list of SSHEntryLogs
    """
    
    def __init__(self, *args) -> None:
        self.logs = []
        for log in args:
            self.logs.append(log)

    def __len__(self) -> int:
        return len(self.logs)

    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.logs)
    
    def __contains__(self, element : SSHLogEntry) -> bool:
        return element in self.logs
    
    def append(self, log : str) -> None:
        self.logs.append(to_SSHLogEntry(log))

    def get(self, starting_data : datetime.datetime, end_data : datetime.datetime) -> List[SSHLogEntry]:
        logs: List[SSHLogEntry] = []
        for log in self.logs:
            if starting_data < log.date < end_data:
                logs.append(log)
        return logs

    def pop(self) -> SSHLogEntry:
        return self.logs.pop(0)

    def __str__(self) -> str:
        return str(self.logs)