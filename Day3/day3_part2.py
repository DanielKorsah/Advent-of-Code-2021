#!/usr/bin/env python

def lst_to_bin(bit_list):
    bin_str = "0b" + "".join(map(str, bit_list))
    return bin_str


def most_common_bit(bitsets):
    mcb = []
    bitsets = list(bitsets)
    for i in range(bit_depth):
        bits = [int(x[i]) for x in bitsets]
        mcb.append(int(sum(bits) >= len(bits) / 2))
    return mcb


def elimination_mcb(bitsets, index=0):
    print("bitsets", bitsets)
    if len(bitsets) == 1 or index == bit_depth:
        return bitsets[0]
    mcb_lst = most_common_bit(bitsets)
    mcb_bin = lst_to_bin(mcb_lst)
    mcb_dec = int(mcb_bin, 2)
    # for each bit string in bitsets, if its bit at the index is the same as most common bit that round,
    # add to remaining
    remaining = [x for x in bitsets if format(mcb_dec ^ int(x, 2), f"0{bit_depth}b")[index] == "0"]

    # longform pseudocode (lol python) explanation of list comprehension for future reference:

    # for group in bitsets:
    #     group_dec = int(group, 2)
    #     print(group, mcb_bin[2:], index)
    #
    #     matched_bit = format(mcb_dec ^ group_dec, f"0{bit_depth}b")[index] == "0"
    #     print(format(mcb_dec ^ group_dec, f"0{bit_depth}b"), matched_bit)
    #     if matched_bit:
    #         remaining.append(group)
    #     print("matched")

    return elimination_mcb(remaining, index + 1)


def elimination_lcb(bitsets, index=0):
    print("bitsets", bitsets)
    if len(bitsets) == 1 or index == bit_depth:
        return bitsets[0]
    mcb_lst = most_common_bit(bitsets)
    mcb_bin = lst_to_bin(mcb_lst)
    mcb_dec = int(mcb_bin, 2)
    remaining = [x for x in bitsets if format(mcb_dec ^ int(x, 2), f"0{bit_depth}b")[index] == "1"]

    return elimination_lcb(remaining, index + 1)


if __name__ == '__main__':
    lines = list(map(str.strip, open("input.txt", "r").readlines()))
    bit_depth = len(lines[0])
    gamma = most_common_bit(lines)

    ones = "0b" + bit_depth * "1"
    gamma_bin = lst_to_bin(gamma)
    gamma_dec = int(gamma_bin, 2)
    epsilon_bin = format(int(ones, 2) ^ int(gamma_bin, 2), f"0{bit_depth}b")
    epsilon_dec = int(epsilon_bin, 2)
    power = gamma_dec * epsilon_dec
    print(gamma_bin, epsilon_bin)
    print(gamma_dec, epsilon_dec, power)

    oxygen = elimination_mcb(lines)
    co2 = elimination_lcb(lines)
    print(oxygen, int(oxygen, 2))
    print(co2, int(co2, 2))
    print("ans: ", int(co2, 2) * int(oxygen, 2))
