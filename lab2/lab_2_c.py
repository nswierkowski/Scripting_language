import sys
from wrong_lines import lines

def print_big():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        the_biggest = ""
        max = 0
        for line in file:
            splited_line = line.split()
            try:
                datas_sent = splited_line[-1]
                if datas_sent != '-' : 
                    the_new = int(datas_sent)
                    if the_new > max:
                        max = the_new
                        the_biggest = splited_line
            except ValueError:
                is_formatted = False
                wrong_formatted_lines.append(line)
            except IndexError:
                is_formatted = False
                wrong_formatted_lines.append(line)
        if is_formatted: print(" ".join(the_biggest[6:-2]) +" "+ str(the_biggest[-1]))
        else: 
            print("ERROR: File is not formatted")
            lines(wrong_formatted_lines)
    except EOFError:
        print("ERROR: I/O exception")

if __name__=="__main__":
    print_big()