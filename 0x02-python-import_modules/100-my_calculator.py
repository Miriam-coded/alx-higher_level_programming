#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    args = len(argv) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
