for a in range(1,5):
    print(a)#Our output will not include 5 since the sequence extends up to 5
else:#The "else" part is optional
    print('The "for" loop is over')

a_1 = 10
while True:
    print('Multiply the number', a_1,'by 2')
    b_1 = int(input('Enter a result:'))
    if b_1 == 20:
        print('You got the right result')
        break#At this point the program will stop to execute another clauses
    else:#The "else" part will not be executed after the "break" statement was called
        print('Try more times')
print('Done')

a_2 = 20
while True:
    b_2 = 2
    c_2 = int(input('Enter a right number:'))
    if c_2 == b_2:
        d_2 = a_2*b_2
        print('Your area of the rectangle is:', d_2)
        break#The "break" statement is at the end, because we will not get the "print()" function
    else:
        print('You should get 40')

l_1 = 30
while True:
    s_1 = input('Enter a text with the length of 30:')
    if len(s_1) == l_1:#"len()" is a function that define a text length
        print('Your text length is', len(s_1))
        break
    elif len(s_1) > l_1:
        print('Your text length is higher than we need')
    else:
        print('Your text length is lower than we need')
print('Done')

while True:
    n_1 = 50
    n_2 = int(input('Eneter a new number:'))
    if n_2 == n_1:
        print('You got the number correct', n_2)
        break
    if n_2 > n_1:
        print('The number is lower than that')

print('Done')

for b in range(1,5):
    if b == 2:
        continue#This command helps us to skip items in the loop
    print(b)
print('We skipped 2')