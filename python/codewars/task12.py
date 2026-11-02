import re


def sum_of_ints(s):
    return sum(int(x) for x in re.findall(r'\d+', s))


print(sum_of_ints('The30quick20brown10f0x1203jumps914ov3r1349the102l4zy'))

