#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argsLength = len(sys.argv[1:])
    if argsLength == 1:
        print("{} argument:".format(argsLength))
    elif argsLength > 1:
        print("{} arguments:".format(argsLength))
    else:
        print("0 arguments.")
    for i in range(1, argsLength + 1):
        print("{}: {}".format(i, sys.argv[i]))
