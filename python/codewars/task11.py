from math import isqrt


def is_square(n):
    if n < 0:
        return False
    else:
        check = False
        for i in range(n, -1, -1):
            if (i ** 2) == n:
                check = True
            else:
                continue
    return check
                

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))

