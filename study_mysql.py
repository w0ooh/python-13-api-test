# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/4/1 22:14
# File   : study_mysql.py
# IDE    : PyCharm

import pymysql

# 1. 建立连接
host = "test.lemonban.com"
user = "test"
password = "test"
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)

# 2. 新建一个查询页面
cursor= mysql.cursor()

# 3. 编写SQL
sql="select max(mobilephone) from future.member"

# 4. 执行SQL
cursor.execute(sql)

# 5. 查看结果
result=cursor.fetchone() #返回最近的一条
print(result)  # result返回的是一个元组，可以用索引来取值
print(result[0])

# 6. 关闭查询
cursor.close()

# 7. 数据库连接关闭
mysql.close()

