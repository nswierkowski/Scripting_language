import argparse
from pathlib import Path
import sys
import ex1
import ex2
import ex4

def run(file, function, min_level):
    if function == 'get_ipv4':
        ex1.read_ssh(file, True, ex2.get_ipv4s_from_log, min_level)
    elif function == 'get_user':
        ex1.read_ssh(file, True, ex2.get_user_from_log, min_level)
    elif function == 'get_message':
        ex1.read_ssh(file, True, ex2.get_message_type_by_line, min_level)
    elif function == 'random_users_logs':
        ex1.read_ssh(file, False, ex4.show_random_users_logs, min_level)
    elif function == 'time_stats':
        ex1.read_ssh(file, False, ex4.all_users_time, min_level)
    elif function == 'active_user':
        ex1.read_ssh(file, False, ex4.most_active_user, min_level)
    

def show():
    parser = argparse.ArgumentParser(description="Logs commander")
    parser.add_argument('file', help="Path to file")
    parser.add_argument('--level', metavar='MIN_LEVEL', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='minimalny poziom logowania (domyślnie INFO)')    
    subparser = parser.add_subparsers(dest='function', help='dostępne funkcje')
    subparser.add_parser('get_ipv4', help='Show ipv4 adresses')
    subparser.add_parser('get_user', help='Show users')
    subparser.add_parser('get_message', help='Show messages')
    subparser.add_parser('random_users_logs', help='Show random users logs')
    subparser.add_parser('time_stats', help='Show statistics on time of use')
    subparser.add_parser('active_user', help='Show most active user')

    args = parser.parse_args()

    file = Path(args.file)
    if not file.exists():
        print("That file doesn't exist")
        raise SystemExit(1)
    
    run(file, args.function, args.level)



if __name__=='__main__':
    show()