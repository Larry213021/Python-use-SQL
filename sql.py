# 以下是MySQL
import pymysql

conn = pymysql.connect(host=  '203.64.95.184', port=3306, user='root', passwd='nkust1108', db='pro_act', charset='utf8')

cursor = conn.cursor()

command = "SELECT * FROM labs"

cursor.execute(command)

data = cursor.fetchmany(5)
print(data)

# command = "INSERT INTO test(id)VALUES(%s)"
# cursor.execute(command,("testing",))
# # 取得第一筆資料
# result = cursor.fetchone()
# print(result)
# conn.commit()

# for i in range(10):
#     print(cursor.fetchone())


cursor.close()
# 關閉資料庫連線
conn.close()

# #以下是MSSQL
# import pymssql
# # 資料庫連線server = '127.0.0.1'
# # DESKTOP-AJMETLV\SQLEXPRESS01
# conn = pymssql.connect(server = '127.0.0.1',user='sa',password='larrylarry52',database='mimic')
# cur = conn.cursor()
# cur.execute('SELECT * FROM mimic.mimic_d_icd_diagnoses$')
#
# for i in range(10):
#     print(cur.fetchone())

