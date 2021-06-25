import sqlite3

conn = sqlite3.connect('items.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM products')
quantity = (len([i for i in cursor.fetchall()]))
cursor.execute('SELECT max(l), max(w), max(h) FROM products')
mp = [(i[0], i[1], i[2]) for i in cursor.fetchall()][0]     # max parameters
volume = mp[0]*mp[1]*mp[2]
result = f'Box params(length, width, height) - ' + str(mp) + ' with ' + str(volume) + ' cub.cm volume.\n' \
        'Total - ' + str(quantity) + ' items to pack.'
print(result)

'''total products volume'''
cursor.execute('SELECT * FROM products')
v = [(i[1]*i[2]*i[3]) for i in cursor.fetchall()]
total = '\n' + 'Total products volume - ' + str(sum(v)) + ' cub.cm.'

file = open('volume.txt', 'w')
file.write(result+total)
file.close()


