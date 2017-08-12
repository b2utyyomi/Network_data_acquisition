# 链接MySQL时，报错：
# can't connect to mysql server through socket '/tmp/mysql.sock'
# 因为我的mysql.sock文件路径不是这个 （通过 find -name mysql.sock 去找它 结果没找到）
# 所以可以做一个软链接：
# ln -s /run/mysqld/mysqld.sock /tmp/mysql.sock
# 就OK啦
# user 为根用户， passwd为其密码。 
import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="512008226226", db="mysql")

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=4")
print(cur.fetchone())
cur.close()
conn.close()
