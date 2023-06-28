from typing import Optional, Union
from ex1 import SSHLogEntry
import re
import datetime

class FailedPassword(SSHLogEntry):
    """
        Class represents log with failed password 
    """
    
    def __init__(self, log: str, date: datetime.datetime, hostName: str, message: str, pID: str) -> None:
        super().__init__(log, date, hostName, message, pID)

    def validate(self) -> bool:
        regex_pattern: str = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match: Optional[re.Match[str]] = re.match(regex_pattern, self.log)
        regex_pattern_failed: str = r'Failed password'
        match_failed: Optional[re.Match[str]] = re.search(regex_pattern_failed, self.message)
        if not match or not match_failed:
            return True
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

    def __init__(self, log: str, date: datetime.datetime, hostName: str, message: str, pID: str) -> None:
        super().__init__(log, date, hostName, message, pID)
    
    def validate(self) -> bool:
        regex_pattern: str = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match: Optional[re.Match[str]] = re.match(regex_pattern, self.log)
        regex_pattern_accepted: str = r'Accepted password'
        match_accepted: Optional[re.Match[str]]  = re.search(regex_pattern_accepted, self.message)
        if not match or not match_accepted:
            return True
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
    
    def __init__(self, log: str, date: datetime.datetime, hostName: str, message: str, pID: str) -> None:
        super().__init__(log, date, hostName, message, pID)
    
    def validate(self) -> bool:
        regex_pattern: str = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match: Optional[re.Match[str]] = re.match(regex_pattern, self.log)
        regex_pattern_to_check_is_there_error: str = r'error'
        match_error: Optional[re.Match[str]] = re.search(regex_pattern_to_check_is_there_error, self.message)
        
        if not match or not match_error:
            return True
        
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

    def __init__(self, log: str, date: datetime.datetime, hostName: str, message: str, pID: str) -> None:
        super().__init__(log, date, hostName, message, pID)

    def validate(self) -> bool:
        regex_pattern: str = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
        match: Optional[re.Match[str]] = re.match(regex_pattern, self.log)
        regex_pattern_else: str = r'Failed password|Accepted password|error'
        match_else: Optional[re.Match[str]] = re.search(regex_pattern_else, self.message)

        if not match:
            return True

        return not (
            datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S') == self.date and
            match.group(2) == self.hostName and
            match.group(3) == self.pID and
            match.group(4) == self.message and
            not match_else
        )

    pass