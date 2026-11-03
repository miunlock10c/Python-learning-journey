user = {
    "name": "Kirril",
    "age": 18,
    #"say_hello": def say_hello(): print("Privet, ya {name}"),
}

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ishuman = True
    def say_hello(self, to_name):
        print(f'Hello {to_name}')




user1 = User("Kirril", 18)# = self in template

print(user1.ishuman)
print(user1.__dict__)
user1.say_hello(to_name='Vasya')
