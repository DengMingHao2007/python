import rsa
import base64

encryptd_msg_str = input("Please enter encryptd msg:")
private_key_str = """-----BEGIN RSA PRIVATE KEY-----
MIICYAIBAAKBgQCTaef74B3vHdnjQOjcOBykhddx6BrOp5Yzc0bxKzGjyRYw8tZX
2HxKMMuoO355eJR10wG/lqNRc78HkllYsbsJd0Re1y/mjvYCU6pdSX7kWPGVnH2I
lbEkwdowROdfKspfBO2p6namT9qRqSZhN2BbudisejqAfWwW7bDFTeEjwQIDAQAB
AoGAURzcLibSsckOJFKKDuq9L/YJZz7cyUtDhYnvxjILPWEfWc21DV8sfLI+zZH2
9KXZor95Xc9ojCARQ/xN5cyFssmvQuJ4mUjXUwqLtfdqYBOycF68EP+6frakKfT3
ouLyfj/jzP/OikQsfZHhiuPFmV9B1M8xiJymxJINtuawlMECRQCULKtCt56x9GNo
Q3fEmdbesBfBsbQpji7eznxt1iEu46J2SNeLLfJEwMXk6I8SvIbUzncOE8k4HS6Y
sezBFPotS1nwuQI9AP6vgnxC5RqaNrkj9YDvE0fXxklgd5qWs3yNp79hCa0bdoUd
7Yh+MMJp5/IpdWUMNnBzfUUZmQ+Uw0H3SQJEJW6TZStV38bJRhGlM/lZGrCJj9kA
lm7g0FCBho3NnDbNV+xW50YYKd45H/bQDf+qYCA4W0oMTyywFMr98FkISmD6u6EC
PQC4i3SBlfdsz1HX1baPNq1B4ZhMkxoXahukpQBoLGhWhw/aZVU5EjdCqHrpfiES
l0bbNNQQvfuqzqCtrAECREp4extfjb3LNaPFmsEohBgETXAltOEoHWKMYf5MarBs
GlX7XO/3MjFqNz1qf3uD0qgXlsuv7jsvGuYYuOJ2mwOZlVj2
-----END RSA PRIVATE KEY-----"""

private_key = rsa.PrivateKey.load_pkcs1(private_key_str.encode())
encryptd_msg = base64.b64decode(encryptd_msg_str.encode())
msg = rsa.decrypt(encryptd_msg, private_key).decode()
print(msg)