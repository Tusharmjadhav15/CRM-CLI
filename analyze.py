import pandas as pd
import sqlite3
import plotly.express as px
conn= sqlite3.connect('db_folder/rtest.db')
curr=conn.cursor()
result=curr.execute('Select lead_remark from sales ').fetchall()
conn.commit()
df=pd.DataFrame(result,columns=['sales'])
valu=df.value_counts().to_list()
names=df['sales'].value_counts().index.to_list()
colors=['gold','red','green','blue','darkpurple']
operation = px.pie(names=names,values=valu,title='Leads Results')
operation.update_traces(textposition='inside',textinfo='percent+label',marker=dict(colors=colors,line=dict(color='#000000',width=1)))
operation.write_html('lead_result.html',auto_open=True)
