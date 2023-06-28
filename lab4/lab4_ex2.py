import os
import sys
from pathlib import Path

def print_exec(dir):
    for file in dir.iterdir():
        path_to_file = os.path.join(dir, file)
        if os.path.isfile(path_to_file) and os.access(file, os.X_OK):
            print("\t" + str(file))


def print_dir(list_of_dir):
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        print("-----------------------------------------------")
        for dir in list_of_dir:
            print(dir)
            dir_path = Path(dir)
            if dir_path.is_dir() :
                print_exec(dir_path)
            print("-----------------------------------------------")

    else:
        print("-----------------------------------------------")
        for dir in list_of_dir:
            print(dir)
            print("-----------------------------------------------")



if __name__=='__main__':
    print_dir(os.environ.get("PATH").split(os.pathsep))
