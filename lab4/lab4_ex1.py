import os
import sys
from numpy import sort

def env_variables(var, argv):
    sort(var)
    if len(argv) > 0:
        argv_set = set(argv)
        for key, value in var.items():
                if key in argv_set:
                    print(f'{key} : {value}')
#

if __name__=='__main__':
    env_variables(os.environ, sys.argv)