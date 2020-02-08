import socket
from threading import Thread

def recv_message(sock):
    while True:
        msg=sock.recv(1024)
        print(msg.decode())#메세지 복호화


sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
sock.connect(("127.0.0.1",12000))#12000번은 연결되는게 아니라 대기만 함. 다른포트 열어줌

th=Thread(target=recv_message, args=(sock,))
th.daemon=True
th.start()

while True:#메시지 주고받음
    msg=input()
    sock.send(msg.encode())

    if msg=="\bye":
        break
sock.close()