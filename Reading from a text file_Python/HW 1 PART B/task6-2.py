import json

items = [1, 2, 3, 4, 5]

new_items = json.dumps(items)
data = {'School': 'Albany', 'Address': '1400 Washington Ave,Albany,NY,1222' , 'Phone': '(518)-442-3300'}

show_items = data.items()
show_items1 = json.dumps(show_items)

show_keys = data.keys()
show_keys1 = json.dumps(show_keys)

show_values = data.values()
show_values1 = json.dumps(show_values)

open('task6-2.txt', 'w').write(new_items + '\n')
file_open=open('task6-2.txt').read()

open('task6-2.txt', 'a').write(show_items1 + '\n')
file_open = open('task3.txt').read()
open('task6-2.txt', 'a').write(show_keys1 + '\n')
file_open = open('task3.txt').read()
open('task6-2.txt', 'a').write(show_values1 + '\n')
file_open = open('task3.txt').read()

print 'Output of items method:',show_items
print 'Output of keys method:',show_keys
print 'Output of values method:',show_values

print 'Output of list: ',new_items