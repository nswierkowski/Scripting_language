import sys
from wrong_lines import lines

def request_code(code):
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        if code == '200' or code == '302' or code == '404':
            number_of_appearances = 0
            for line in file:
                try:
                    if line.split()[-2] == code:
                        number_of_appearances += 1
                except IndexError:
                     is_formatted = False
                     wrong_formatted_lines.append(line)
            if is_formatted : print(f"{number_of_appearances} requests")
            else : 
                print(f"{number_of_appearances} requests but file is not correctly formatted, so this result doesn't have to be correct")
                lines(wrong_formatted_lines)
        else : 
            print("There is no request with this code")
    except EOFError:
            print("ERROR: I/O exception")