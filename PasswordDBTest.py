# import pymysql
# conn = pymysql.connect(host='sql6.freemysqlhosting.net', port=3306,
#                        user='sql6498570', passwd='AJ6NHabilg', db='sql6498570')
# cur = conn.cursor()

# sql = """insert into MagsHealthApp (name, email, pswdHash, weight)
#          values (%s, %s, %s, %s)
# """
# cur.execute(sql, ("John", "email1@gmail.com", "password1", 100))
# conn.commit()

# getPWhash = "SELECT `pswdHash` FROM MagsHealthApp WHERE `email`=%s"
# cur.execute(sql, ('email1@gmail.com'))
# result = cur.fetchone()
# print(result)

# Signup Code
# sql = """insert into MagsHealthApp (name, email, pswdHash, weight)
#         values (%s, %s, %s, %s)
# """
# hashed = bcrypt.hashpw(input(), bcrypt.gensalt())
# cur.execute(sql, ("John", "email1@gmail.com", hashed, 100))
# conn.commit()

import bcrypt
# Get hash from string
# password = bytes(input("password?\n").strip(), 'utf-8')
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashed)

# Check hashed
hashpwd = b'$2b$12$p0MDY.8BY0nkSZxWzOzflufv2IiI0Tr1/OZdIVz8wTAc.PFfo6C52'
userpwd = bytes(input("password?\n").strip(), 'utf-8')
if bcrypt.checkpw(userpwd, hashpwd):
    print("match")
