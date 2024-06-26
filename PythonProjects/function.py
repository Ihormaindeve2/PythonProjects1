def hello():
    print('Hello')
hello()#We call the function right after it had been created

def numberSum(x,y):#We add the specific "parameters" for this function
    print(x+y)
numberSum(2,5)#We expect the output will be 5

def average(x,y):
    c = (x+y)/2#We calculate the average number
    print(c)
average(3,7)#We should get 5 since (3+7=10 and 10/2=5)

def printMin(x,y):#We will define the minimum number out of the given numbers
    if x > y:
        print('The minimum is:', y)
    else:
        print('The minimum is:', x)
printMin(3, 5)#The output should be 3

def printLoop(x):
    if x > 0:#The number should be positive
        c_1 = 0
        for c_1 in range(1, x):#We will create a "for" loop from the user's input
            print(c_1)
    else:
        print('The number should be positive')
printLoop(7)#We should get a loop such as:(1, 2, 3, 4, 5, 6)

def local_function1(x):
    x = 5#We create a local variable that defined only in this function
    print('Local value in this function is:', x)
x = 7
print(x)#We should get 7
local_function1(7)#We should get 5 since the "x" value is a local variable

def local_function2(x):
    x = 5
    if x > 3:
        print('The local value is:', x)
x_1 = 7
print(x_1)#We will get 7
local_function2(3)#We will get 5

def global_function1():
    global x#We defined the global variable so, we can assign to this variable anything outside the function
    print('x is equal to', x)
x = 30
global_function1()#We should get 30 since we are using the global variable

def global_function2():
    global x
    if x == 3:
        x = 4#We changed the variable to the local by assigning something in the function
        print('We changed the global variable to local, and the value is:', x)
    else:
        print('x is equal to:', x)
x = 5
global_function2()#We should get 5 since we have the global variable
x = 3
global_function2()#We should get 4 since we changed the global variable to the local variable

def default_function1(x, y=1):#We assign the default argument for the "y" value
    print(x*y)
default_function1(2)#We should get 2 since we didn't use the default argument
default_function1(2, 5)#The output should be 10 as we used the default arguments

def default_function2(x, y=1):#We create the default argument
    if x == 2:
        print('The sum is:', x+y)#We will get a sum of numers
    else:
        b_2 = 0
        for b_2 in range(y, x):
            print(b_2)
        print('The loop is over')
default_function2(2)#We will get 3 since we should get a sum
default_function2(3)#We should get a loop of numbers such as:(1,2)