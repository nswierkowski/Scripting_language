import sys

def ratio():
     try:
          file = sys.stdin
          gif = 0
          jpg = 0
          jpeg = 0
          xbm = 0
          for line in file:
               extension = line.split()[-4].split('.')[-1]
               if extension == 'gif': gif += 1
               elif extension == 'jpg': jpg += 1
               elif extension == 'jpeg': jpeg += 1
               elif extension == 'xbm': xbm += 1
          print(f'| gif  \t | jpg \t | jpeg\t| xbm \t| \n|{gif} | {jpg} | {jpeg} | {xbm} | ')
     except EOFError:
          print("ERROR: I/O exception")

if __name__=="__main__":
    ratio()