print('Crete your own password')
print('Your password should starts with an upper case letter, it should contains the number in it, and it should be at least 10 characters long')
while True:
    password1 = input('Type your password here:')
    if password1.islower() == False and password1.isnumeric() == False and len(password1) > 10:
        print("Congratulations, you've created your own password:", password1)
        break
    elif len(password1) < 10:
        print('Your password should contain at least 10 characters')
    else:
        print('Try again')

print('Your password is:', password1)
print('Now, you will create your login')
data1 = {}
while True:
    name1 = input('Type your name here:')
    if name1.isdigit() == False and name1.isnumeric() == False:
        if name1.islower() == True:
            print('Your name is:', name1.capitalize())
            break
        else:
            print('Your login is:', name1)
        break
    else:
        print('Try again')

data1.update({name1: password1})
print('Your data is:', data1.keys(), 'and', data1.values())
