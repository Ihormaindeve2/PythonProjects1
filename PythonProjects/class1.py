class Person:
    pass #Indicates an empty block 
p = Person()
print(p)

class Person1:
    def sayHi(self):
        print('Hello, how are you?')

p = Person1()
p.sayHi()

class Person2:
    def __init__(self, name):
        self.name = name
    def sayHi1(self):
        print('Hello, my name is:', self.name)

p = Person2('Swaroop')
p.sayHi1()