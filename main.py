import requests
import mysql.connector

url = "https://saddam-teacher-api.onrender.com/internet/clean?token=saddam_teacher"

response = requests.get(url)
data = response.json()

db = mysql.connector.connect(
    host='localhost',
    user='user',
    password='1234',
    database='uztelecom_db'
)

cursor = db.cursor()

for row in data:
    sql = """ INSERT INTO clients(user_id,fio,holat,oylik_tolov,tarif,tezlik_mbps,
    ulangan_sana,year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (
        row['user_id'],
        row['fio'],
        row['holat'],
        row['oylik_tolov'],
        row['tarif'],
        row['tezlik_mbps'],
        row['ulangan_sana'],
        row['year']
    )
    cursor.execute(sql, values)
db.commit()
cursor.close()
db.close()
print("Tayyor boldi !")

