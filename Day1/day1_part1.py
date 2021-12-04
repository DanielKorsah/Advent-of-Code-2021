#!/usr/bin/env python
depths = list(map(int, open("input.txt", "r").readlines()))
count_inc = 0
for i in range(1, len(depths)):
    count_inc += depths[i] > depths[i - 1]
print(count_inc)
