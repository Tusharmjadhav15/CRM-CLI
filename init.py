import pandas as pd
import numpy as np

ss=[''.join(np.random.choice(list("987654321"),10)) for _ in range(50)]
name = ["".join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'),10)) for _ in range(50)]
df = pd.DataFrame({
    'Names':name,
    'Mobile': ss,
    'Status': 0 ,
    'result':'unhandled'

})
df.to_csv('db_folder/data1.csv',index=False)