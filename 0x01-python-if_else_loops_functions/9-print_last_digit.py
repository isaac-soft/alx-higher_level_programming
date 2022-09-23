#!/usr/bin/python3

def print_last_digit(number):
    number = number * -1 if number < 0 else number
    print("{}".format(str(number)[-1]), end="")
    return str(number)[-1]
