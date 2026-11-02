def count_by(n, x):
    return [i for i in range(x, (x * n) + 1, x)]


print(count_by(5, 10))
