#!/usr/bin/env python
lines = list(map(str.strip, open("input.txt", "r").readlines()))
lst = []
gamma = []
bit_depth = len(lines[0])
for i in range(bit_depth):
    lst = [int(x[i]) for x in lines]
    gamma.append(int(sum(lst) >= len(lst) / 2))

ones = "0b" + bit_depth * "1"
gamma_bin = "".join(map(str, gamma))
gamma_dec = int(gamma_bin, 2)
epsilon_bin = format(int(ones, 2) ^ int(gamma_bin, 2), f"0{bit_depth}b")
epsilon_dec = int(epsilon_bin, 2)
print(gamma_bin, epsilon_bin)
print(gamma_dec, epsilon_dec, gamma_dec * epsilon_dec)
