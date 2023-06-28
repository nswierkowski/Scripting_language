import pytest
import datetime
import ipaddress
from ex7 import to_SSHLogEntry
from ex7 import SSHLogJournal
from ex2 import FailedPassword, AcceptedPassword, Error, ElseInfo

@pytest.mark.parametrize(
    "log, time", [
        (
            "Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth]",
            datetime.datetime.strptime("Dec 10 07:11:42", '%b %d %H:%M:%S')
        ),
        (
            "Dec 10 13:46:55 LabSZ sshd[4882]: Received disconnect from 81.144.235.98: 11: Bye Bye [preauth]",
            datetime.datetime.strptime("Dec 10 13:46:55", '%b %d %H:%M:%S')
        ),
        (
            "Jan  4 05:54:08 LabSZ sshd[19770]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.87.109.156  user=root",
            datetime.datetime.strptime("Jan  4 05:54:08", '%b %d %H:%M:%S')
        )
    ])
def test_to_SSHLogEntry_time(log, time):
    assert to_SSHLogEntry(log).date == time

@pytest.mark.parametrize(
    "log, ipv4", [
        (
            "Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth] 0.0.0.0",
            ipaddress.IPv4Address("0.0.0.0")
        ),
        (
            "Dec 10 13:46:55 LabSZ sshd[4882]: Received disconnect from 81.144.235.98: 11: Bye Bye [preauth]",
            ipaddress.IPv4Address("81.144.235.98")
        ),
        (
            "Jan  4 05:54:08 LabSZ sshd[19770]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.87.109.156  user=root",
            ipaddress.IPv4Address("218.87.109.156")        
        )
    ])
def test_ipv4(log, ipv4):
    assert to_SSHLogEntry(log).get_ipv4() == ipv4

@pytest.mark.parametrize(
    "log, ipv4", [
        (
            "Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth] 256.256.256.256",
            None
        ),
        (
            "Dec 10 13:46:55 LabSZ sshd[4882]: Received disconnect from 81.644.235.98: 11: Bye Bye [preauth]",
            None
        ),
        (
            "Jan  4 05:54:08 LabSZ sshd[19770]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=256.256.109.156  user=root",
            None        
        )
    ])
def test_ipv4_incorrect(log, ipv4):
    assert to_SSHLogEntry(log).get_ipv4() == ipv4

@pytest.mark.parametrize(
    "log, ipv4", [
        (
            "Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth]",
            None
        ),
        (
            "Dec 10 13:46:55 LabSZ sshd[4882]: Received disconnect from: 11: Bye Bye [preauth]",
            None
        ),
        (
            "Jan  4 05:54:08 LabSZ sshd[19770]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=  user=root",
            None        
        )
    ])
def test_ipv4_none(log, ipv4):
    assert to_SSHLogEntry(log).get_ipv4() == ipv4

@pytest.mark.parametrize(
    "log_list, log, log_type", [
        (
            SSHLogJournal(),
            "Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth]",
            type(ElseInfo("Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth]", datetime.datetime.strptime("Dec 10 07:11:42", '%b %d %H:%M:%S'), "LabSZ", "input_userauth_request: invalid user chen [preauth]", "24224"))
        ),
        (
            SSHLogJournal(),
            "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2",
            type(FailedPassword("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2", datetime.datetime.strptime("Dec 10 06:55:48", '%b %d %H:%M:%S'), "LabSZ", "Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2", "24200"))
        ),
        (
            SSHLogJournal(),
            "Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2",
            type(AcceptedPassword("Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2", datetime.datetime.strptime("Dec 10 09:32:20", '%b %d %H:%M:%S'), "LabSZ", "Accepted password for fztu from 119.137.62.142 port 49116 ssh2", "24680"))        
        ),
        (
            SSHLogJournal(),
            "Dec 10 11:03:44 LabSZ sshd[25455]: error: Received disconnect from 103.99.0.122: 14: No more user authentication",
            type(Error("Dec 10 11:03:44 LabSZ sshd[25455]: error: Received disconnect from 103.99.0.122: 14: No more user authentication", datetime.datetime.strptime("Dec 10 11:03:44", '%b %d %H:%M:%S'), "LabSZ", "error: Received disconnect from 103.99.0.122: 14: No more user authentication", "25455"))        
        )
    ])
def test_append(log_list, log, log_type):
    log_list.append(log)
    assert type(log_list.pop()) == log_type
