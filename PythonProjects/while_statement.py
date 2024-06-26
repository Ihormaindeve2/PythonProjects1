a = 13
b = 24
running = False#We are indicating that "while" loop was satrted
while running:
    c_1 = int(input('Enter a number 1:'))
    c_2 = int(input('Enter a number 2:'))
    if a == c_1 and b == c_2:
        print('You guessed all numbers')
        running = False#This indicates that "while" loop was finished
    elif a != c_1 or b != c_2:
        print('You guessed not all numbers, try to guess some more times')
print('Done')