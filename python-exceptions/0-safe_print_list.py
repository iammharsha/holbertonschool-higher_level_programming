#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i], end="")
            count++
        print()
        return count
    except:
        print()
        return count
