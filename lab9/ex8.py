import re
import datetime
from typing import Optional

class SSHUser:

    def __init__(self, name: str, date_of_last_login: datetime.datetime) -> None:
        self.name = name
        self.date_of_last_login = date_of_last_login
    
    def validate(self) -> bool:
        regex_pattern: str = r'^[a-z_][a-z0-9_-]{0,31}$'
        match: Optional[re.Match[str]] = re.search(regex_pattern, self.name)
        if match:
            return False
        else:
            return True
        