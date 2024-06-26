groceryStore1 = {
    'storage1': 'red apple',
}

print('We have only', groceryStore1['storage1'], 'in our dictionary')
groceryStore1.update({'storage2': 'strawberries'}) #Method 'update()' insert only one new key/value pair in our dictionary
groceryStore1.update({'storage3': 'bananas'})
print('All our storages in our dictionary are:', groceryStore1.keys()) #Method 'keys()' returns a list of the keys from the dictionary
print('All our storages contain:', groceryStore1.values()) #This method returns a list of all values in the dictionary
groceryStore1.update({'price': 1400})
price1 = groceryStore1.get('price') #This method return the value of the specified key
print('The price for the whole storage is:', price1)
print('I will buy the whole storage of the', groceryStore1['storage1'])
groceryStore1.pop('storage1') #This method removes the last key/value pair with the specified keys
groceryStore1['price'] = 700
print('All our items in our dictionary are:')
for product, value in groceryStore1.items():
    print(product, value)

print('We will create another grocery store')
groceryStore2 = groceryStore1.copy() #This method returns a copy of the whole dictionary
print('We will add more items and their prices in our grocery store')
groceryStore2.update({'cucumbers': 110})
groceryStore2.update({'tomatoes': 75})
groceryStore2.update({'potatoes': 35})
print('Right now our grocery store contain:')
for item, price in groceryStore2.items():
    print(item, price)

print('We will buy all our items in our grocery store')
groceryStore2.clear() #The method 'clear()' removes all items from the dictionary
print("So, we don't have anything in our grocery store")
