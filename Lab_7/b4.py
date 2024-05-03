#Từ điển:
inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#Thêm key 'pocket':
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#Sắp xếp các phần tử trong 'backpack' key:
inventory['backpack'].sort()

#Loại bỏ 'dagger' khỏi 'backpack' key:
inventory['backpack'].remove('dagger')

#Thêm 50 vào 'gold:
inventory['gold'] += 50

#Kết quả:
print(inventory)