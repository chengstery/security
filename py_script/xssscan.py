# coding:utf-8

from urllib.parse import urlsplit, urlparse, parse_qs
import requests


class xss_scanner():
    def __init__(self, url):
        # self.url=input('输入尝试的url:')   #获取url
        self.url = url  # 获取url
        res = requests.get(self.url, timeout=10)  # 测试url是否可以使用
        if res.status_code == 200 or res.status_code == 301:
            print('可以正常访问')
        else:
            print('访问失败')
            exit()

    def xss_dict(self):
        palyords = []
        types = []
        with open('./dict/xss-payload.txt', 'r') as fp:
            xss = fp.readlines()
            for x in xss:
                type = x.strip().split(':', 1)[0]
                x = x.strip().split(':', 1)[1]
                types.append(type)
                palyords.append(x)
            return types, palyords  # 遍历xss字典，存储到列表里，方便后面使用

    def xss_html(self):
        # url=urlsplit(self.url).query
        # pattern=r'(\w+)=([^&]+)'   #\w前面以=号为界限，后面以&开头
        # res=re.findall(pattern,url)   #先正则表达式，在str
        # paly=(dict(res))   #使用正则表达式取出palyord值，字典存储

        # Parse the URL using urlparse
        parsed_url = urlparse(self.url)
        # Get the query parameters as a dictionary
        query_params = parse_qs(parsed_url.query)

        return query_params

    def excape(self, text, hex=False):
        if hex:
            encoded_text = "".join(f"&#x{ord(char):x};" for char in text)
        else:
            encoded_text = "".join(f"&#{ord(char)};" for char in text)
        return encoded_text

    def xss_url(self):
        paly = self.xss_html()
        types, pyloads = self.xss_dict()
        for k in paly:
            for type, pyload in zip(types, pyloads):
                if type == 'Escape':
                    pyload = self.excape(pyload)
                if type == 'Cookie':
                    cook = requests.get(url=self.url).cookies
                    ck = dict(cook).keys()
                    cookie = {str(*ck): pyload}
                    u = requests.get(url=self.url, cookies=cookie).text  # request获取

                elif type == 'Referer' or type == 'User-Agent':
                    header = {type: pyload}
                    u = requests.get(url=self.url, headers=header).text  # request获取
                else:
                    psram = {k: pyload}
                    u = requests.get(url=self.url, params=psram).text  # request获取
                res = u.lower().find(pyload.lower())  # xss成功的话，会找到注入的字典内容
                end = u[res - 2:res - 1]
                if res != -1 and end != '=' and type == 'Normal':
                    print(f'url:{self.url} 当前xss成功:{pyload}')
                elif res != -1 and end == '=' and type == 'Prop':
                    print(f'url:{self.url} 当前xss成功:{pyload}')
                elif res != -1:
                    print(f'url:{self.url} 当前xss成功:{pyload}')


if __name__ == '__main__':
    xss_scanner = xss_scanner('http://192.168.88.150:8080/xss-labs/level3.php?keyword=test')
    xss_scanner.xss_url()
