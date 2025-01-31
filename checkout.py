import uuid
import sqlite3
import pandas as pd
from datetime import datetime
conn = sqlite3.connect('db_folder/rtest.db')
curr = conn.cursor()
res=curr.execute('select *  from bda where name == \'{}\''.format('tushar')).fetchone()
result=curr.execute('Select lead_remark from sales where lead_remark = \'Interested\' ').fetchall()
len(result)
rate=2000
payout = len(result)*rate
today = datetime.now().strftime('%y-%m-%d') 
print("|-------------------------------------------+--------------------------+--------------------------------------------------------|")
print("|-------------------------------------------| Welcome to Checkout page |--------------------------------------------------------|")
print("|-------------------------------------------+--------------------------+--------------------------------------------------------|")


donelead= curr.execute('SELECT lead_name, lead_mobile,lead_remark from sales where lead_stats=1').fetchall()
print("+--------------------------+")
print("|Total Handled Leads : ",len(donelead),'|')
print("+--------------------------+")
rlead= curr.execute('SELECT lead_name, lead_mobile,lead_remark from sales where lead_stats=0').fetchall()
print("+-----------------------------+")
print("|Total Remaining Leads : ",len(rlead),'|')
print("+-----------------------------+")             
print()
print("+---------------------------------------+")             
print('|PAYOUT : TOTAL INTERESTED LEADS * 2000 |')
print("+---------------------------------------+")             
print('|PAYOUT :               ',payout ,'     Paid |')
print("+---------------------------------------+")             
curr.execute('INSERT INTO bda_payouts values(?,?,?,?,?)',(str(uuid.uuid4()),res[0],today,'Salary Paid',payout))
conn.commit()
print("+-------------------------------------------+--------------------------+--------------------------------------------------------+")
print('|                                           |THANKYOU FOR YOUR HARDWORK|                                                        |')
print("+-------------------------------------------+--------------------------+--------------------------------------------------------+")