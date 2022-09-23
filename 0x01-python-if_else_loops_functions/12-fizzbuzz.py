#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" " if i < 99 else "")
        elif i % 3 == 0:
            print("Fizz", end=" " if i < 99 else "")
        elif i % 5 == 0:
            print("Buzz", end=" " if i < 99 else "")
        else:
            print(i, end=" " if i < 99 else "")
