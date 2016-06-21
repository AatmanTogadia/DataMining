import json

items = [1, 2, 3, 4, 5]

new_items = json.dumps(items)

items2 = [6, 7, 8, 9, 10]

new_items2 = json.dumps(items2)

open('task4.txt', 'w').write(new_items)
file_open=open('task4.txt').read()

open('task4.txt','a').write(new_items2)
file_open=open('task4.txt').read()


print items
print new_items2