def sum_without_minmax(ar: list):
    if ar is None or len(ar) <= 1:
        return 0
    ar.remove(min(ar))
    ar.remove(max(ar))
    return sum(ar)


print(sum_without_minmax([9, 1, 3, 4, 5, 6]))
