#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string,str):
        return 0
    rom_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    total = 0
    prev_num = 0
    for ch in reversed(roman_string):
        num = rom_int.get(ch)
        if not num:
            return 0
        if num < prev_num:
            total -= num
        else:
            total += num
        prev_num = num
    return total
