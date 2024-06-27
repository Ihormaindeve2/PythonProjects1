data1 = ['Ihor', 'Vladimir', 'Kostya']
print('The items from 0 to the end are:', data1[:]) #We'll get everything that we have in the list above
data1.append('Nikita')
print('The items from 0 to 2 are:', data1[0:2]) #We'll get items in range (0, 2), but the index 2 will be not executed
name1 = data1[1]
print('The letters from 1 to 3 are:', name1[1:3]) #We can slice strings as well
print('The letters from 2 to the end are:', name1[2:])
print('The whole name is:', name1[:])