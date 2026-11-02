def double_char(s):
    result = []
    for i in s:
        result.append(i)
        result.append(i)
    total = ''.join(result)
    return total


print(double_char("HEllo"))

