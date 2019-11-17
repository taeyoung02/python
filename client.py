import socket

#서버 IP & port
ip = 192.168.5.56
port = 9999

#클라이언트 소켓 준비
client = socket.socket()

#서버접속
clinet.connet((ip,port))
print('----- server is conneceted-----')

#메세지 송신
client.sent(b'Hello~~ i\'m clinet')
print(' -------Message received-----')

#메시지 수진
msg = client.recv(1024)
print(' -------Message received------')
print(msg)

clinet.close()