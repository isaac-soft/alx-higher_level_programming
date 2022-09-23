#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        # skip combination repetitions
        if i >= j:
            continue
        # break 1st loop if at the last combination
        if i == max(range(10)) - 1:
            break
        # print combinations
        print("{}{}".format(i, j), end=", ")
    # break second loop if at the last combination
    if i == max(range(10)) - 1:
        break
# print the last combination
print("{}{}".format(i, j))

# Alternatively
# for num in range(9):
#   for var in range(num + 1, 10):
#       print("{:d}{:d}".format(num, var), end = '\n' if num == 8 else ', ')
