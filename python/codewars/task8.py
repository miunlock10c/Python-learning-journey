def string_repeat(n: int, s: str):
    if n >= 1:
        return n * s
    else:
        return ''


print(string_repeat(4, 'a'))
print(string_repeat(3, 'hello'))
print(string_repeat(2, 'abc'))
print(string_repeat(0, ''))
print(string_repeat(0, 'I'))
print(string_repeat(5, ''))
print(string_repeat(6, 'I'))
print(string_repeat(5, 'Hello'))
