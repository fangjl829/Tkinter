
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/31 08:56
# !/usr/bin/python3
# -*- coding:utf-8 -*-


#保存一个班级的学生信息,根据学生学号‘1002’查询学生
#一个班级的学生信息是多条数据，必须使用能够保存多条数据的类型  列表 元组  字典  集合
#学生信息(sno sname age score)

#1列表保存学生信息,学生信息使用元组保存
stus=[('1001','张三',23,98),
      ('1002', '李四', 23, 99)]

#1列表保存学生信息,学生信息使用字典
stus=[{'sno':'1001','sname':'张三','age':23,'score':98},
      {'sno': '1002', 'sname': '李四', 'age': 23, 'score': 99},]

#如果使用列表保存学生信息，必须遍历当前列表，拿学号进行判断，时间复杂度O(n)
for stu in stus:
    pass #获取到当前学号进行判断

#字典保存学生信息
stus={'1001':{'sname':'张三','age':23,'score':98},
      '1002':{'sname': '李四', 'age': 23, 'score': 99}}
#如果使用的使用字典保存,根据key进行获取,时间复杂度O(1)
stu=stus['1002']
