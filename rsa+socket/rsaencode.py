import rsa,base64

public_key, private_key = rsa.newkeys(2048)
public_key_str = public_key.save_pkcs1()
private_key_str = private_key.save_pkcs1()

msg = input('Please enter massenge:')
public_key = rsa.PublicKey.load_pkcs1(public_key_str.decode())
encryptd_msg = rsa.encrypt(msg.encode(), public_key)

encryptd_msg_str = base64.b64encode(encryptd_msg).decode()

print(private_key_str.decode())
print(encryptd_msg_str)