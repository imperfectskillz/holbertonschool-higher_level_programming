#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)-1
    if arg == 0:
        print("{} arguments.".format(arg))
    elif arg == 1:
        print("{} argument:".format(arg))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg))
        for i in range(1, arg+1):
            print("{}: {}".format(i, argv[i]))
