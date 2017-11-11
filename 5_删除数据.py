
import sqlite3

# 连接数据库 如果没有就会创建
conn = sqlite3.connect('my.db')

# 创建cursior对象 光标
cursor = conn.cursor()

# 插入一条数据
cursor.execute('delete from user where id = \'100002\'')

# 查询数据
cursor.execute('select * from user')
l = cursor.fetchall()
print(l)

# 打印row的行数
print(cursor.rowcount)

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭数据库
conn.close()
