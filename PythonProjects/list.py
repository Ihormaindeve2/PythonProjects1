shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'item to purchase')
print('These items are:')
for item in shoplist:
    print(item)
print('\n I also have to buy rice')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shoppin list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)