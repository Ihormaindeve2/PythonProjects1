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

class Person3:
    '''Represents a person.'''
    population = 0
    def __init__(self, name):
        '''Initialize the person's data.'''
        self.name = name
        print('Initializing', self.name)
        #When this person is created, he/she
        #adds to the population
        Person3.population += 1
    def __del__(self):
        '''I am dying.'''
        print(self.name, 'says bye')
        Person3.population -= 1
        if Person3.population == 0:
            print('I am the last one.')
        else:
            print('There are still', Person3.population, 'people left.')
    def sayHi(self):
        '''Greeting by the person
        Really, that's all it does.'''
        print('Hi, my name is', self.name)
    def howMany(self):
        '''Prints the current population'''
        if Person3.population == 1:
            print('I am the only person here.')
        else:
            print('We have', Person3.population, 'person here')

swaroop = Person3('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person3('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()