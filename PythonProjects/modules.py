import module1
import module2
module1.sayhi()
print('Version is', module1.version)

def math_operation():
    a = int(input('Enter a first number:'))
    b = int(input('Enter a second number:'))
    if a < b:
        print(module2.addtition(a,b))
    elif a > b:
        print(module2.subtraction(a,b))
    elif a == b:
        print(module2.multiplication(a,b))
math_operation()