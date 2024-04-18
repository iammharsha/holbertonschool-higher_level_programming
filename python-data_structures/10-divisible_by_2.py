#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible = list(my_list)
    for i in range(len(my_list)):
        divisible[i] = my_list[i] % 2 == 0
    return divisible
