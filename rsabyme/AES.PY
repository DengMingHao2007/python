from crypto import Random
from crypto.Hash import SHA
from crypto.Cipher import AES
from crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from crypto.PublicKey import RSA
import base64


# 秘钥
key = 'chenqichenqi1234'

# 明文
raw = 'sina company11111111111111111111'

# 加密
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
data = iv + cipher.encrypt(raw)


# 解密
iv = data[:16]
cipher = AES.new(key, AES.MODE_CFB, iv)
print (cipher.decrypt(data[16:]))