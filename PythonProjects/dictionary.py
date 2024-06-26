ab = {
    'Swaroop': 'swaroopch@byteofpython.info',
    'Larry' : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer' : 'spammer@hotmail.com'
} #We should use a curly brackets in order to assign the dictionary
print("Swaroop's address is", ab['Swaroop'])
ab['Guido'] = 'guido@python.org'
del ab['Spammer'] #We can delete items in the dictionary
print('\n There are', len(ab), 'contacts in the address-book')
for name, address in ab.items():
    print('Contact', name, 'at', address)
if 'Guido' in ab:# We use 'in' statement in order to check if this item exists in the dictionary
    print("\n Guido's address is", ab['Guido'])
