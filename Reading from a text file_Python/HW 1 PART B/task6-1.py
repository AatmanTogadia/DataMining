import json
data = {'School': 'Albany', 'Address': '1400 Washington Ave,Albany,NY,1222' , 'Phone': '(518)-442-3300'}

show_items = data.items()
show_items1 = json.dumps(show_items)

show_keys = data.keys()
show_keys1 = json.dumps(show_keys)

show_values = data.values()
show_values1 = json.dumps(show_values)

open('task6-1.txt', 'w').write(show_items1 + '\n')
file_open = open('task6-1.txt').read()
open('task6-1.txt', 'a').write(show_keys1 + '\n')
file_open = open('task6-1.txt').read()
open('task6-1.txt', 'a').write(show_values1 + '\n')
file_open = open('task6-1.txt').read()

print 'Output of items method:',show_items
print 'Output of keys method:',show_keys
print 'Output of values method:',show_values