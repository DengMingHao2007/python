import binascii

byte_var = '中'.encode('utf-8') 

print('Byte variable: ', byte_var)
print('Hexadecimal: ',binascii.hexlify(byte_var))
byte_var = binascii.hexlify(byte_var)
byte_var = int(byte_var)
print("unhex:",binascii.unhexlify(byte_var))
byte_var=binascii.unhexlify(byte_var)

byte_var = byte_var.decode('utf-8')
print(byte_var)
print(type(byte_var))