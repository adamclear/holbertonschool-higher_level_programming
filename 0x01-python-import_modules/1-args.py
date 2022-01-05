#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("0 arguments.")
    elif len(sys.argv) == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        x = 0
        print("{} arguments:".format(len(sys.argv)))
        for i in len(sys.argv):
            print("{}: {}".format(x + 1, sys.argv[x]))
