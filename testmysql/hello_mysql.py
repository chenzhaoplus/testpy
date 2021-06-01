# 查询mysql表
import mysql.connector

mydb = mysql.connector.connect(
    host="172.16.4.83",
    user="ibmp_test",
    passwd="XZdfjXIEsrumGrfFTmfltbtAuQCECUdl",
    database="ibmp"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM basic_person")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    break
