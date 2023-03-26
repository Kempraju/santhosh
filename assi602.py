class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def sayHi(dog):
    print(f'Hi, my name is {dog.name} and I am {dog.age} years old!')

d = Dog('Dot', 4)

sayHi(d) 
