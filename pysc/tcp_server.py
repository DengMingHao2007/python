
import socket
server = socket.socket()
server.bind(("localhost",6969)) #绑定要监听的端口port
server.listen(5) # 监听，这里表示最多有5个客户端连接服务器，python2不好使
print('waiting the call')
while True:
    conn,addr = server.accept() # 等电话打进来，每个conn代表一个客户端的连接
    print(conn)
    print('the call has comming')
    while True:
        data = conn.recv(1024)
        if not data :
            print('this user is end,exit!\n next user')
            break
        print('data:',data.decode())
        conn.send(data.upper())