#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        if i == max(range(10)) - 1:
            break
        print("{}{}".format(i, j), end=", ")
    if i == max(range(10)) - 1:
        break
print("{}{}".format(i, j))
