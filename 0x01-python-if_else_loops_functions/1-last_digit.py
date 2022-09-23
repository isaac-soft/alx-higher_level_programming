#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# extract the last digit
if number >= 0:
    last_digit = int(str(number)[-1])
if number < 0:
    last_digit = int(str(number)[-1]) * -1
# setting the text property for each condition
if last_digit > 5:
    text = "and is greater than 5"
elif last_digit == 0:
    text = "and is 0"
elif (last_digit < 6) and (last_digit != 0):
    text = "and is less than 6 and not 0"
# print the output
print("Last digit of {} is {} {}".format(number, last_digit, text))
