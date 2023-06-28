import ipaddress
import re
from abc import ABC
from abc import abstractmethod

class SSHLogEntry(ABC):
    """
        Class represents a single log
    """

    def __init__(self, log, date, hostName, message, pID) -> None:
        self.log = log
        self.date = date
        self.hostName = hostName
        self.message = message
        self.pID = pID
    
    def __str__(self):
        return self.log
    
    def get_ipv4(self):
        regex_pattern = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
        address = re.search(regex_pattern, self.message)
        if address:
            return ipaddress.IPv4Address(address.group(0))
        else:
            return None
        
    @property
    def has_ip(self):
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

    def __len__(self):
        return len(self.log)

    @abstractmethod
    def validate(self):
        pass
