import sys
from wrong_lines import lines

def total_size():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        size = 0
        for line in file:
                try:
                    datas_sent = line.split()[-1]
                    if datas_sent != '-' : size += int(datas_sent)
                except ValueError:
                    is_formatted = False
                    wrong_formatted_lines.append(line)
                except IndexError:
                    is_formatted = False
                    wrong_formatted_lines.append(line)
        size = size/1000000000
        if is_formatted : print(f"Total amount of data sent is {size} gigabytes")
        else : 
            print(f"Total amount of data sent is {size} gigabytes but file is not formatted correctly so it doesn't have to be a correct result")
            lines(wrong_formatted_lines)
    except EOFError:
        print("ERROR: I/O exception")

if __name__=="__main__":
    total_size()