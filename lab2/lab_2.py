import sys

if __name__=="__main__":
    try:
        for line in sys.stdin:
            sys.stdout.write(line)
    except EOFError:
        print("ERROR: I/O exception")