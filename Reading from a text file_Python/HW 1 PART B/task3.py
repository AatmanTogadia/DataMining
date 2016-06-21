import json

items = [1, 2, 3, 4, 5]

#f = open('task3.txt', 'w')

#dump_list = json.dumps(items)

open('task3.txt', 'w').write(json.dumps(items))

load_items = json.loads(open('task3.txt').read())

print items