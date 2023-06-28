import sys
import re
from ex3 import show_log
                
def to_dictionery(line):
    regex_pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'
    match = re.match(regex_pattern, line)
    return {
        'date': match.group(1),
        'hostname': match.group(2),
        'id': match.group(3),
        'message': match.group(4)
    }

def get_ipv4s_from_log(line):
    regex_pattern = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    return re.findall(regex_pattern, line['message'])

def get_user_from_log(line):
    regex_pattern = r'user (\w+)|user=\w+|Accepted password for (\w+)'
    match1 = re.search('Accepted password for (\w+)', line['message'])
    match2 = re.search('user (\w+)', line['message'])
    if match1:
        return match1.group(0).split()[-1]
    if match2:
        return match2.group(1)
    return None

def get_message_type(message):
    regex_pattern = r'POSSIBLE BREAK-IN ATTEMPT|Accepted|Failed password|Connection closed|Invalid user|Disconnecting|preauth|session closed'
    match = re.search(regex_pattern, message)
    if match:
        return match.group(0)
    else:
        return "inne"

def get_message_type_by_line(line):
    return get_message_type(line['message'])    

if __name__=='__main__':
    line = 'Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!'
    line2 = 'Dec 10 13:46:40 LabSZ sshd[4772]: Accepted password for fztu from 113.118.187.34 port 30950 ssh2'
    line3 = 'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2'
    dic = to_dictionery(line2)
    print(get_user_from_log(dic))

