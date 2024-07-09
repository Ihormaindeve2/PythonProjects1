dataBase1 = {}
print("You have nothing stored in your dataBase:", len(dataBase1))
while True:
    key1 = str(input('Type your key for the database:'))
    if type(key1) == str:
        print('Your key is:', key1)
        break
    else:
        print('You should type a word')
print('You have written your key')

print('Now, enter your value for your keyword, but your value should not be longer than 10 letters')
while True:
    value1 = str(input('Enter the value of your keyword:'))
    if len(value1) < 10:
        print('Your value is:', value1)
        dataBase1.update({key1: value1})
        break
    else:
        print('Your value shoud not be longer than 10 letters')
print('You have stored', len(dataBase1), 'element in your dictionary', dataBase1[key1])



