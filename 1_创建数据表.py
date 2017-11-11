
import sqlite3

# 连接数据库 如果没有就会创建
conn = sqlite3.connect('my.db')

# 创建cursior对象 光标
cursor = conn.cursor()

# 执行sql语句 创建一个数据表 user
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一条数据
cursor.execute('insert into user (id,name) values (\'100001\',\'AdleyTales\')')

# 打印row的行数
print(cursor.rowcount)

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭数据库
conn.close()
