#!/usr/bin/env python
lines = list(map(str.strip, open("input.txt", "r").readlines()))
depth = 0
pos = 0
aim = 0

for line in lines:
    command, val = line.split(" ")
    val = int(val)

    if command == "forward":
        pos += val
        depth += aim * val
    elif command == "down":
        aim += val
    elif command == "up":
        aim -= val

print(depth, pos, depth * pos)
