import sys
from wrong_lines import lines

def host_pl():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        for line in file:
            try:
                after_dot = line.split()[0].split('.')[-1]
                if after_dot == 'pl': 
                    sys.stdout.write(line)
            except IndexError:
                is_formatted = False
                wrong_formatted_lines.append(line)
    except EOFError:
        print("ERROR: I/O exception")
    if not is_formatted : 
        print("File is not correctly formatted")
        lines(wrong_formatted_lines)   

if __name__=="__main__":
    host_pl()