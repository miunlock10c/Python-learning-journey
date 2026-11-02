user = {'name': "kirill", 'age': 18}
try:
    print(user['email'])
except KeyError:
    raise ValueError("Key email doesnt exist")
