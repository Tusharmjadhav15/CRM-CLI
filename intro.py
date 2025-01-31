import sqlite3
import pandas as pd
import uuid
from datetime import datetime

conn = sqlite3.connect('db_folder/rtest.db')
print()
print()
print('+--------------------------------------------------------------------------------------------------------------------------------------+')
print('|                                                 | Databases Successfully Connected|                                                  |')
print('+--------------------------------------------------------------------------------------------------------------------------------------+')
curr= conn.cursor()
print()
print()
name = input("Enter your name: ")
print()
print()
res=curr.execute('select *  from bda where name == \'{}\''.format(name)).fetchone()
if len(res)==0:

    print("wrong answer")
else:
    bda_idd = curr.execute('select (id) from bda where name == \'{}\''.format(name)).fetchone()
    print('+----------------------------------------------+---------------------------------+-----------------------------------------------+')
    print('|----------------------------------------------|                                 |-----------------------------------------------|')
    print("|                                              | welcome! ", name ,"To CRM Panel   |                                               |")
    print('|----------------------------------------------|                                 |-----------------------------------------------|')
    print('+----------------------------------------------+---------------------------------+-----------------------------------------------+')
# conn.commit()




df=pd.read_csv('db_folder/data1.csv')
names = df['Names']
id=[str(uuid.uuid4()) for _ in range(len(names))]
mobile = df['Mobile']
status=[0 for _ in range(len(names))]
result=['unhandled' for _ in range(len(names))]
bda_id=[bda_idd[0] for _ in range(len(names))]
lead_date=[datetime.now().strftime('%d-%m-%Y') for _ in range(len(names))]
data=list()
for i in range(len(names)):
    temp=(id[i],bda_id[i],names[i],str(mobile[i]),int(status[i]),result[i],lead_date[i])
    data.append(temp)
#print(data)
# conn = sqlite3.connect('db_folder/rtest.db')
# curr = conn.cursor()
#try
curr.executemany('insert into sales values(?,?,?,?,?,?,?)',data)
print()
print()

print('+--------------------------------------------+---------------------------------------+--------------------------------------------------+')
print('|                                            | DATA SUCCESSFULLY STORED IN DATABASES |                                                  |')
print('+--------------------------------------------+---------------------------------------+--------------------------------------------------+')
conn.commit()
