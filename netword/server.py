import sys
import socket
#创建socket对象
socketserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
socketserver.bind((host,port))
socketserver.listen(5)
while True:
    clientserver,addr=socketserver.accept()
    print("地址为%s" %str(addr))
    msg="欢迎访问"
    clientserver.send(msg.encode("utf-8"))
    clientserver.close()
