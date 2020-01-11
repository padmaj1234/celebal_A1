import MySQLdb
import pandas as pd

def insertVariblesIntoTable(id,city,pin,office_id):
        connection = MySQLdb.connect(host='localhost',
                                             database='padmaj',
                                             user='root')
        insert = "insert into data1 (ID, Cities, Pincode, Office_id)" \
                "values(%s,%s,%s,%s)"
        cursor = connection.cursor()
        print(cursor)
        record = (id,city,pin,office_id)
        cursor.execute(insert,record)
        connection.commit()
        print("Record inserted successfully into Laptop table")
        

df = pd.read_csv('/home/padmaj/dataset1.csv')
for i in range(0,300):
    insertVariblesIntoTable(df['ID'][i],df['Cities'][i],df['Pincode'][i],df['Office_ID'][i])
