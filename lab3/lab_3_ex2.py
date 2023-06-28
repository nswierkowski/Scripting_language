import sys
from datetime import datetime
import re
from typing import Tuple
from typing import List
from lab_3_ex3 import *

def read_log(file):
    logs = []
    month = {
        'Jun':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
    i = 0
    for line in file:
        elem_str = tuple(line.split())
        data = re.split(r'[/:]', elem_str[3])
        try:
            #element = (address, datetime, -0400], extension, code, bytes)
            if len(elem_str) == 10 and elem_str[-1].isdigit():
                elements = (elem_str[0], 
                            datetime(int(data[2]), 
                                    month[data[1]], 
                                    int(data[0][1:]), 
                                    int(data[3])), 
                            elem_str[4], 
                            elem_str[6], 
                            int(elem_str[-2]), 
                            int(elem_str[-1]))
                logs.append(elements)
            elif len(elem_str) == 9 and elem_str[-1].isdigit():
                elements = (elem_str[0], 
                            datetime(int(data[2]), 
                                    month[data[1]], 
                                    int(data[0][1:]), 
                                    int(data[3])), 
                            elem_str[4], 
                            elem_str[6], 
                            int(elem_str[-2]), 
                            int(elem_str[-1]))
                logs.append(elements)
            else:
                elements = (elem_str[0], 
                            datetime(int(data[2]), 
                                    month[data[1]], 
                                    int(data[0][1:]),
                                    int(data[3]), 
                                    int(data[4]), 
                                    int(data[5])), 
                            elem_str[4], 
                            elem_str[6], 
                            int(elem_str[-2]), 
                            0)
                logs.append(elements)
        except ValueError:
             print('value - '+str(elem_str))
        except IndexError:
            print('index - '+str(elem_str))
    return logs

def sort_log(log, index):
     if not log : 
         print("NoneTypeError in sort_log: This list is empty I suppose")
         return
     log.sort(key=lambda x: x[index])

def print_entries(log):
    if not log:
        print("NoneTypeError in print_entries: Empty list!")
        return
    for line in log:
        print(str(line))

def get_entries_by_addr(log, addr):
    try:
        return [line for line in log if line[0] == addr]
    except IndexError:
        print("IndexError in get_entries_by_addr")

def get_entries_by_code(log, code):
    try:
        return [line for line in log if line[-2] == code]
    except IndexError:
        print("IndexError in get_entries_by_code")

def get_failed_reads(log, combine_lists):
    code_4xx = []
    code_5xx = []
    for line in log:
        code = line[-2]
        if 400 <= code < 500:
            code_4xx.append(code)
        if 500 <= code < 600:
            code_5xx.append(code)
    if combine_lists: 
        return code_4xx.append(code_5xx)
    else:
        return code_4xx, code_5xx
    
def get_entires_by_extension(log, extension):
    new_log = []
    for line in log:
        ex = line[-3].split('.')[-1]
        if ex == extension[1:]:
            new_log.append(line)
    return new_log


if __name__=='__main__':
    list_of_tuple = []
    try:
        list_of_tuple = read_log(sys.stdin)
    except EOFError:
        print("aaaaaa python panic")

    #list_of_tuple = get_entries_by_addr(list_of_tuple, "199.120.110.21")
    #sort_log(list_of_tuple, 0)
    #list_of_tuple = get_entries_by_code(list_of_tuple, 200)
    #list_of_tuple = get_failed_reads(list_of_tuple, True)
    #list_of_tuple = get_entires_by_extension(list_of_tuple, '.jpg')
    #print_entries(list_of_tuple)

    #print(str((entry_to_dict(list_of_tuple))))
    #print(str(log_to_dict(list_of_tuple)))

    list_of_dict = log_to_dict(list_of_tuple)
    #print(str(list_of_dict))
    #print(str(get_addrs(list_of_dict)))
    print_dic_entry_dates(list_of_dict)

    
