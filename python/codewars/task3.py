def RemoveExclamationMarks(string):
    test = []
    for i in string:
        if i == '!':
            continue
        else:
            test.append(i)
    result = ''.join(test)
    return result


print(RemoveExclamationMarks("Hello world !"))
