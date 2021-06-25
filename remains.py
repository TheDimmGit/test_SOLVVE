import sqlite3
import csv
import pandas as pd


conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# cursor.execute(f"""CREATE TABLE IF NOT EXISTS warehouses
#                     (id INTEGER PRIMARY KEY,
#                     name text
#                     )
#                     """)
# cursor.execute(f"""CREATE TABLE IF NOT EXISTS items
#                     (id INTEGER PRIMARY KEY,
#                     name text,
#                     qty integer,
#                     warehouse_id integer
#                     )
#                     """)

cursor.execute('SELECT * FROM items WHERE warehouse_id=1 ')
items = [(i[1], i[2]) for i in cursor.fetchall()]
items_list = [i[0] for i in items]
qty_list = [i[1] for i in items]
names_dict = [{'name': i} for i in items_list]
qty_dict = [{'qty': i} for i in qty_list]
for i, j in enumerate(names_dict):
    j.update(qty_dict[i])


print('\n---Warehouse 1 items:---\n')

for i in items:
    di = {i[0]: i[1]}
    print(str(i[0]) + ', QTY - ' + str(i[1])+'\n'+'---------------')

with open("warehouse1.csv", "w", newline='') as f:
    fieldnames = ['name', 'qty']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(names_dict)


with open('warehouse1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print('\n'+str(row))


cursor.execute('SELECT * FROM items WHERE warehouse_id=2 ')
items = [(i[1], i[2]) for i in cursor.fetchall()]
items_list = [i[0] for i in items]
qty_list = [i[1] for i in items]
names_dict = [{'name': i} for i in items_list]
qty_dict = [{'qty': i} for i in qty_list]
for i, j in enumerate(names_dict):
    j.update(qty_dict[i])


print('\n---Warehouse 2 items:---\n')

for i in items:
    di = {i[0]: i[1]}
    print(str(i[0]) + ', QTY - ' + str(i[1])+'\n'+'---------------')

with open("warehouse2.csv", "w", newline='') as f:
    fieldnames = ['name', 'qty']
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    writer.writerows(names_dict)


with open('warehouse2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print('\n'+str(row))


cursor.execute('SELECT * FROM items WHERE warehouse_id=3 ')
items = [(i[1], i[2]) for i in cursor.fetchall()]
items_list = [i[0] for i in items]
qty_list = [i[1] for i in items]
names_dict = [{'name': i} for i in items_list]
qty_dict = [{'qty': i} for i in qty_list]
for i, j in enumerate(names_dict):
    j.update(qty_dict[i])


print('\n---Warehouse 3 items:---\n')

for i in items:
    di = {i[0]: i[1]}
    print(str(i[0]) + ', QTY - ' + str(i[1])+'\n'+'---------------')

df = pd.DataFrame(names_dict, columns=['name', 'qty'])                         # PANDAS
print(df)

# with open("warehouse3.csv", "w", newline='') as f:                           # CSV
#     # fieldnames = ['name', 'qty']
#     # writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
#     # writer.writeheader()
#     # writer.writerows(names_dict)


# with open('warehouse3.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print('\n'+str(row))


