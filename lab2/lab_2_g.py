import sys
import re
from wrong_lines import lines

def friday():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        for line in file:
            try:
                date = line.split()[3]
                date = re.split('[ |]|/|:', date)
                day = int(date[0][1:])
                if 1 <= day <= 28 and (day - 3) % 7 == 0 and date[1] == 'Jul' and date[2] == '1995':  
                    sys.stdout.write(line)
            except ValueError:
                is_formatted = False
                wrong_formatted_lines.append(line)
            except IndexError:
                is_formatted = False
                wrong_formatted_lines.append(line)
    except EOFError:
        print("ERROR: I/O exception")
    if not is_formatted : 
        print("File is not correctly formatted")
        lines(wrong_formatted_lines)   


if __name__=="__main__":
    friday()