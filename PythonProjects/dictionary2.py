store = {
    'bananas': 400,
    'apples': 100,
    'strawberries': 350,
    'cherries': 270,
    'mangos': 130
}
print('We have', len(store), 'items at our store')
weight = store['apples'] + store['strawberries'] + store['bananas'] + store['cherries'] + store['mangos']
print('The total weight of all our items is:', weight, 'pounds')
print('We sold all bananas today, so our list right nwo is:')
del store['bananas']
for products, items in store.items():
    print(products, items, 'pounds')
print('We got new vegetables now')
store['tomatoes'] = 350
store['cucumbers'] = 270
store['onion'] = 170
print('Now our store has items such as:')
for products, items in store.items():
    print(products, items, 'pounds')
print('We need to compare the weight of fruits and vegetables so, we will create two lists and each of these list will contain the weight of fruits and vegetables')
fruitsWeight = []
vegetablesWeight = []
print('Right now our lists are empty', fruitsWeight, vegetablesWeight)
fruitsWeight.append(store['apples'])
fruitsWeight.append(store['strawberries'])
fruitsWeight.append(store['cherries'])
fruitsWeight.append(store['mangos'])
vegetablesWeight.append(store['tomatoes'])
vegetablesWeight.append(store['cucumbers'])
vegetablesWeight.append(store['onion'])
print('Our fruit list is:', fruitsWeight)
print('Our vegetable list is:', vegetablesWeight)
print("Let's sort our items in each list")
fruitsWeight.sort()
vegetablesWeight.sort()
print('Our sorted fruit list is:', fruitsWeight)
print('Our sorted vegetable list is:', vegetablesWeight)
print('We divided all our items in the separate lists so, now we can compare them')
def compare(a,b):
    if type(a) == list and type(b) == list:
        c_1 = a[0] + a[1] + a[2] + a[3]
        c_2 = b[0] + b[1] + b[2]
        if c_1 > c_2:
            print('The', c_1, 'pounds of fruits is greater than', 'the', c_2, 'pounds of vegetables')
        elif c_1 < c_2:
            print('The', c_2, 'pounds of vegetables is greater than',  'the', c_1, 'pounds of fruits')
        else:
            print('The', c_1, 'pounds of fruits is the same as', 'the', c_1, 'pounds of vegetables')
print("Let's compare our items")
print(compare(fruitsWeight, vegetablesWeight))


