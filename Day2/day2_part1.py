#!/usr/bin/env python
lines = list(map(str.strip, open("input.txt", "r").readlines()))
depth = 0
pos = 0

for line in lines:
    command, val = line.split(" ")

    if command == "forward":
        pos += int(val)
    elif command == "down":
        depth += int(val)
    elif command == "up":
        depth -= int(val)

print(depth, pos, depth * pos)
