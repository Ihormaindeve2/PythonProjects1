def minimum(x,y):
    if x > y:
        return y
    else:
        return x
print(minimum(3,2)) #We should get 2 as our minimum number

def average(a,b,c):
    d_1 = (a + b + c)/2
    if d_1 > a:
        return d_1
    else:
        return a
print(average(1, 2, 3)) #We should get 3 as our average

def list():
    b_1 = int(input('Enter a number 1:'))
    b_2 = int(input('Enter a number 2:'))
    if b_1 < 0:
        print('The number should be a positive')
    elif b_1 > 0:
        for i in range(b_1, b_2):
            if b_1 == b_2:
                break
            elif b_1 != b_2:
                print(i)#We should get a list of numbers
list()
print('Loop is over')