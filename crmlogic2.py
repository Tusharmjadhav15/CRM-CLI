import pandas as pd
import sqlite3
conn = sqlite3.connect('db_folder/rtest.db')
curr = conn.cursor()
rl= 'SELECT * FROM sales WHERE lead_stats = 0;'
dl= 'SELECT * FROM sales WHERE lead_stats = 1;'
remainingl =curr.execute(rl).fetchall()
print()
print()
print("+-------------------------------------------+----------------------+------------------------------------------------------------+")
print("|-------------------------------------------| Welcome to CRM Panel |------------------------------------------------------------|")
print("+-------------------------------------------+----------------------+------------------------------------------------------------+")
while(True):
    
    

    print()
    print("1. Handle Next Leads")
    print("2. Show Handled Leads")
    print("3. Show Remaining Leads")
    print("4. Exit")
    choice = input("Enter your Choice : ")
    print()

    if choice=='1':
        if len(remainingl)==0:
            print("No more Remaining leads!")
            break
        clead = curr.execute(rl).fetchone()
        print("+--------------------------+")
        print("|Names      |  Phone Number|")
        print("+--------------------------+")
        print("|{} | {}   |".format(clead[2],clead[3]))
        print("+--------------------------+")
        print()
       
        print("+----------------------------------------+-----------------------+-----------------------------------------------------------+")
        print("|----------------------------------------|Enter Customer Response|-----------------------------------------------------------| ")
        print("+----------------------------------------+-----------------------+-----------------------------------------------------------+")
        print()
        print("+-----------------+")
        print("|1.Interested     |")
        print("|-----------------|")
        print("|2.Not Interested |")
        print("|-----------------|")
        print("|3.DNP            |")
        print("|-----------------|")
        print("|4.Call back later|")
        print("+-----------------+")
        print()
        inp = int(input("Enter your response => "))
       
        if(inp == 1):
            result="Interested"
            curr.execute('Update  sales set lead_stats = 1 , lead_remark = \'{}\'  where id=\'{}\''.format(result,clead[0]))
        elif(inp == 2):
            result="Not Interested"
            curr.execute('Update  sales set lead_stats = 1 ,lead_remark = \'{}\'  where id=\'{}\''.format(result,clead[0]))
        elif(inp == 3):
            result="DNP"
            curr.execute('Update  sales set lead_stats = 1 ,lead_remark = \'{}\'  where id=\'{}\''.format(result,clead[0]))
        elif(inp == 4):
            result="Call back later"
            curr.execute('Update  sales set lead_stats = 1 , lead_remark = \'{}\'  where id=\'{}\''.format(result,clead[0]))
        else:
            print("Invalid Input! Please Try Again")

        conn.commit()

    elif choice=='2':
        donelead= curr.execute('SELECT lead_name, lead_mobile,lead_remark from sales where lead_stats=1').fetchall()
        print("Total Handled Leads : ",len(donelead))
        print()
        print('+-----------------------------------+')
        print("|   Name     |  Mobiles   | Result  |")
        print('+-----------------------------------+')
        for i in range(len(donelead)):
            print("| {}| {} | {} ".format(donelead[i][0],donelead[i][1],donelead [i][2]))
        print("\n")
        conn.commit()
    elif choice=='3':
        rleads= curr.execute('SELECT lead_name, lead_mobile,lead_remark from sales where lead_stats=0').fetchall()
        print("Remaining Leads: ",len(rleads))
        print()
        print("Name       |     Mobiles| Result")
        for i in range(len(rleads)):
            print("{} | {} | {}".format(rleads[i][0],rleads[i][1],rleads[i][2]))
        print()
        
        conn.commit()
    elif choice=='4':
        print("+-------------------------------------------------------------------------------------------------------------------------------+")
        print("|                                               Thank you! For working Hard                                                     |")
        print("+-------------------------------------------------------------------------------------------------------------------------------+")
        
        conn.commit()
        break

