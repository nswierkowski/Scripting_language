from SSHLogEntryClass import SSHLogEntry
import re
import datetime

class FailedPassword(SSHLogEntry):
    """
        Class represents log with failed password 
    """
    
    def __init__(self, log, date, hostName, message, pID) -> None:
        super().__init__(log, date, hostName, message, pID)

    def validate(self):
        regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match = re.match(regex_pattern, self.log)
        regex_pattern_failed = r'Failed password'
        match_failed = re.search(regex_pattern_failed, self.message)
        return not (
            datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S') == self.date and
            match.group(2) == self.hostName and
            match.group(3) == self.pID and
            match.group(4) == self.message and
            match_failed
        )
        

    pass

class AcceptedPassword(SSHLogEntry):
    """
        Class represents log with accepted password 
    """

    def __init__(self, log, date, hostName, message, pID) -> None:
        super().__init__(log, date, hostName, message, pID)
    
    def validate(self):
        regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match = re.match(regex_pattern, self.log)
        regex_pattern_accepted = r'Accepted password'
        match_accepted = re.search(regex_pattern_accepted, self.message)
        return not (
            datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S') == self.date and
            match.group(2) == self.hostName and
            match.group(3) == self.pID and
            match.group(4) == self.message and
            match_accepted
        )
    pass

class Error(SSHLogEntry):
    """
        Class represents log with an error 
    """
    
    def __init__(self, log, date, hostName, message, pID) -> None:
        super().__init__(log, date, hostName, message, pID)
    
    def validate(self):
        regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match = re.match(regex_pattern, self.log)
        regex_pattern_to_check_is_there_error = r'error'
        match_error = re.search(regex_pattern_to_check_is_there_error, self.message)
        return not (
            datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S') == self.date and
            match.group(2) == self.hostName and
            match.group(3) == self.pID and
            match.group(4) == self.message and
            match_error
        )
    pass

class ElseInfo(SSHLogEntry):
    """
        Class represents log with else information
    """

    def __init__(self, log, date, hostName, message, pID) -> None:
        super().__init__(log, date, hostName, message, pID)

    def validate(self):
        regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match = re.match(regex_pattern, self.log)
        regex_pattern_else = r'Failed password|Accepted password|error'
        match_else = re.search(regex_pattern_else, self.message)
        return not (
            datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S') == self.date and
            match.group(2) == self.hostName and
            match.group(3) == self.pID and
            match.group(4) == self.message and
            not match_else
        )

    pass