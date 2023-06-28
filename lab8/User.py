import re

class SSHUser:

    def __init__(self, name, date_of_last_login) -> None:
        self.name = name
        self.date_of_last_login = date_of_last_login
    
    def validate(self):
        regex_pattern = r'^[a-z_][a-z0-9_-]{0,31}$'
        match = re.search(regex_pattern, self.name)
        if match:
            return False
        else:
            return True
        