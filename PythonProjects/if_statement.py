#We created two variables and assign some numbers to them
a = 13
b = 14
if a > b:#We add an "if" statement to our program
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is the same as b')
print('end')

a_1 = 14#We created two variables for calculating whether the area or the perimeter of the rectangle
b_1 = 12
if a_1 > b_1:
    c = a_1*b_1#We calculate the are of the rectangle
    print('The area of the rectangle is', c)
elif a_1 < b_1:
     c = 2*(a_1+b_1)#We calculate the perimeter of the rectangle
     print('The perimeter of the rectangle is', c)
else:
    c = 2*(a_1+b_1)/2#We calculate the *semiperimeter of the rectangle
    print('The semiperimeter of the rectangle is', c)
print('end')

a_2 = int(input('Enter a number:'))
'''We used a function called "input" to give
a user an opportunity to type any number that he/she wants to type'''
b_2 = int(input('Enter a number:'))
'''We add "int" before "input" since we need to use 
the numbers not strings, otherwise we wil work with string, which could lead to the error when we
will combine our numebrs together'''
if a_2 > b_2:
    c = (a_2+b_2)/2#We calculate the average number
    print('The average is', c)
elif a_2 < b_2:
    print(b_2)#The output will be the greater number
else:
    print(a_2,'=',b_2)
print('end')