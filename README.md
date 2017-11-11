# python操作sqlite

> sqlite 是一种文件形式的数据库,经常被集成到应用程序当中，常见的TV等大型设备上都广泛使用！python与nodejs一样，只需要引入相应的sqlite3的驱动包，就可以操作sqlite了。无需安装。

## 创建一个数据库+表

```py

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

```

## 插入数据 insert

```py


  import sqlite3

  # 连接数据库 如果没有就会创建
  conn = sqlite3.connect('my.db')

  # 创建cursior对象 光标
  cursor = conn.cursor()

  # 插入一条数据
  cursor.execute('insert into user (id,name) values (\'100003\',\'Adley_app\')')

  # 打印row的行数
  print(cursor.rowcount)

  # 关闭cursor
  cursor.close()

  # 提交事务
  conn.commit()

  # 关闭数据库
  conn.close()


```

## 查询数据 search

```py

  import sqlite3

  # 连接数据库 如果没有就会创建
  conn = sqlite3.connect('my.db')

  # 创建cursior对象 光标
  cursor = conn.cursor()

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


```

## 修改数据 update

```py

  import sqlite3

  # 连接数据库 如果没有就会创建
  conn = sqlite3.connect('my.db')

  # 创建cursior对象 光标
  cursor = conn.cursor()

  # 插入一条数据
  cursor.execute('update user set name = \'xiaoming\' where id = \'100003\'')

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


```

## 删除数据 delete

```py


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


```
