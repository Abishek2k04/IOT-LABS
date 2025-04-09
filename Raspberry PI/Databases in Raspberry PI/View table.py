import sqlite3
import pandas as pd
conn=sqlite3.connect("Temperature.db")
cursor=conn.cursor()
query=cursor.execute("select * from TempData")
cols=[column[0] for column in query.description]
result=pd.DataFrame.from_records(data=query.fetchall(),columns=cols)
print(result)
conn.commit()
conn.close()
