#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    prev_value = 0    
    if roman_string is None or not isinstance(roman_string, str):
        return ans
    for char in reversed(roman_string):
        value = roman[char]
        if value < prev_value:
            ans -= value
        else:
            ans += value
        prev_value = value
    return ans
