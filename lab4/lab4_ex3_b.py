import sys
from pathlib import Path
import os
import csv
import subprocess

def history_list(backup):
    backup_history = os.path.join(backup, 'history.csv')
    if os.path.exists(backup_history):
        with open(backup_history, mode='r') as file:
            return list(csv.DictReader(file))
    return []

def remove_old(file_path):
    for root, dirs, files in os.walk(file_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def unzip(file_path, backup_file):
    archive = os.path.join(file_path, backup_file)
    subprocess.run(['unzip', archive, '-d', file_path])
    os.remove(archive)

def restore(file_path = Path.cwd(), backup = str(os.environ.get("BACKUPS_DIR"))):
    his = history_list(backup)
    if len(his) > 0:
        for i,row in enumerate(his):
            print(f'{i+1}. {row["date"]} - {row["directory"]} - {row["name"]}')
    choice = int(input("Which number you want to restore? "))-1
    if choice >= len(his) or choice < 0:
        print("ERROR: Wrong input")
        return restore(file_path, backup)
    remove_old(file_path)
    zip = ''.join([his[choice]['name'], '.zip'])
    path_to_backup = os.path.join(backup, zip)
    subprocess.call(f'cp -r "{path_to_backup}" "{file_path}"', shell=True)
    unzip(file_path, zip)

if __name__=='__main__':
    if len(sys.argv) > 2:
        restore(Path(sys.argv[1]), Path(sys.argv[2]))
    elif len(sys.argv) > 1:
        restore(Path(sys.argv[1]))
    else:
        restore()