import sys
from wrong_lines import lines

def ratio():
    is_formatted = True
    wrong_formatted_lines = []
    try:
        file = sys.stdin
        graphic = 0
        non_graphic = 0
        for line in file:
            try:        
                extension = line.split()[-4].split('.')[-1]
                if extension == 'gif' or extension =='jpg' or extension =='jpeg' or extension =='xbm': graphic += 1
                else: non_graphic += 1
            except IndexError:
                is_formatted = False
                wrong_formatted_lines.append(line)
        div = graphic/non_graphic
        if is_formatted : 
            print(f'Graphic to non graphic: {div}')
        else :
            print(f"Graphic to non graphic: {div} but some line was skipped")
            lines(wrong_formatted_lines)
    except EOFError:
        print("ERROR: I/O exception")
    except ZeroDivisionError:
         print(f"Infinite (there is no non graphic files and {graphic} graphic files)")

if __name__=="__main__":
    ratio()