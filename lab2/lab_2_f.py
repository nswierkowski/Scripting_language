import sys
from wrong_lines import lines

def time():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        for line in file:
                try:
                    hour = int(line.split(" ")[3].split(':')[1])
                    if 22 <= hour < 24 or 0 <= hour < 6:
                        sys.stdout.write(line)
                except IndexError:
                    is_formatted = False
                    wrong_formatted_lines.append(line) 
                except ValueError:
                    is_formatted = False
                    wrong_formatted_lines.append(line) 
    except EOFError:
        print("ERROR: I/O exception")
    if not is_formatted : 
        print("File is not correctly formatted")
        lines(wrong_formatted_lines)   
        
if __name__=="__main__":
    time()