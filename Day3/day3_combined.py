#!/usr/bin/env python

def lst_to_bin(bit_list):
    bin_str = "0b" + "".join(map(str, bit_list))
    return bin_str


def mcb_list(bitsets):
    mcb = []
    bitsets = list(bitsets)
    for i in range(bit_depth):
        bits = [int(x[i]) for x in bitsets]
        mcb.append(int(sum(bits) >= len(bits) / 2))
    return mcb


def mcb_decimal(bits):
    mcb_lst = mcb_list(bits)
    mcb_bin = lst_to_bin(mcb_lst)
    mcb_dec = int(mcb_bin, 2)
    return mcb_dec


def elimination(gamma, epsilon, index=0):
    print("gamma", gamma)
    print("epsilon", epsilon)
    if len(gamma) == 1 and len(epsilon) == 1 or index == bit_depth:
        return gamma[0], epsilon[0]

    if len(gamma) > 1:
        mcb_dec = mcb_decimal(gamma)
        gamma = [x for x in gamma if format(mcb_dec ^ int(x, 2), f"0{bit_depth}b")[index] == "0"]
    if len(epsilon) > 1:
        mcb_dec = mcb_decimal(epsilon)
        epsilon = [x for x in epsilon if format(mcb_dec ^ int(x, 2), f"0{bit_depth}b")[index] == "1"]
    return elimination(gamma, epsilon, index + 1)


def most_least(bitset):
    gamma_dec = mcb_decimal(bitset)
    ones = "0b" + bit_depth * "1"
    epsilon_bin = format(int(ones, 2) ^ gamma_dec, f"0{bit_depth}b")
    epsilon_dec = int(epsilon_bin, 2)
    return gamma_dec, epsilon_dec


if __name__ == '__main__':
    lines = list(map(str.strip, open("input.txt", "r").readlines()))
    bit_depth = len(lines[0])

    g, e = most_least(lines)
    power = g * e
    oxygen, co2 = elimination(lines, lines)
    print("power", bin(g), g, bin(e), e, power)
    print("oxygen", oxygen, int(oxygen, 2))
    print("co2", co2, int(co2, 2))
    print("ans: ", int(co2, 2) * int(oxygen, 2))
