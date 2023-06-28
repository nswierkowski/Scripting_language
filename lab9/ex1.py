import datetime
import ipaddress
import re
from abc import ABC
from abc import abstractmethod
from typing import List, Union

class SSHLogEntry(ABC):
    """
        Class represents a single log
    """

    def __init__(self, log: str, date: datetime.datetime, hostName: str, message: str, pID: str) -> None:
        self.log = log
        self.date = date
        self.hostName = hostName
        self.message = message
        self.pID = pID
    
    def __str__(self):
        return self.log
    
    def get_ipv4(self) -> Union[ipaddress.IPv4Address, None]:
        regex_pattern: str = r'\b(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])(?:\.(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])){3}\b'
        address: Union[re.Match[str], None] = re.search(regex_pattern, self.message)
        if address:
            return ipaddress.IPv4Address(address.group(0))
        else:
            return None
        
    @property
    def has_ip(self) -> bool:
        if self.get_ipv4():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        return self.log == other.log

    def __lt__(self, other):
        return self.date < other.date
    
    def __gt__(self, other):
        return self.date > other.date

    @abstractmethod
    def validate(self) -> bool:
        pass
