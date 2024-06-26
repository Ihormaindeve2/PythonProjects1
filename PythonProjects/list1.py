list1 = []
while True:
    a_1 = int(input('Type just positive number:'))
    if a_1 < 0:
        print('You typed a negative number')
    else:
        list1.append(a_1)
        print('Your number is', list1[0])
        break
