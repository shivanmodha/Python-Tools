''' Module to parse through string '''
import sys
import ConColors

def main():
    ''' Program Entry Point '''
    if len(sys.argv) >= 1:
        for line in sys.stdin:
            ln = line[]
            print (line)
    else:
        for line in sys.stdin:
            print (sys.argv[1])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(ConColors.BLUE + "Interruption Detected" + ConColors.BLACK)
