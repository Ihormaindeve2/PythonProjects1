print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist #"Mylist" is just another name pointing to the same object
del shoplist[0]
print('shoplist is:', shoplist)
print('Mylist is:', mylist)
print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
print('shoplist is:', shoplist)
print('mylist is:', mylist)