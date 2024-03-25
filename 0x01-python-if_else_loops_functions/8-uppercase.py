#!/usr/bin/python3

def uppercase(str):

    for j in str:
        print("{}".format(chr(ord(j) - 32) if ord(j) >= 97 and
              ord(j) <= 122 else j), end="")
    print()
