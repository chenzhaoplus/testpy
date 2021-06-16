# 查询mysql表
# 安装不然会报错 pip install mysql-connector
import mysql.connector

mydb = mysql.connector.connect(
    host="172.16.4.83",
    user="ibmp_test",
    passwd="XZdfjXIEsrumGrfFTmfltbtAuQCECUdl",
    database="ibmp"
)


def select():
    print(mydb)

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM basic_person")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        break
